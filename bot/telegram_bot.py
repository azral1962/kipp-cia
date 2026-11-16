"""Bot Telegram pilihan: hanya perintah, tanpa menyimpan pesan atau memakai LLM."""
from __future__ import annotations
import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import BufferedInputFile, Message
from dotenv import load_dotenv
from kipp.catalog import AKAR, load_catalogue, search_catalogue

DEMO = AKAR / "04-alur-kerja" / "DEMO_TERINTEGRASI.md"
LOGGER = logging.getLogger(__name__)
STATUS = {
    "draft": "draf",
    "in_review": "dalam tinjauan",
    "beta": "beta",
    "verified": "terverifikasi",
    "deprecated": "tidak dianjurkan",
}


async def bantuan(pesan: Message) -> None:
    await pesan.answer(
        "Bot katalog KIPP-CIA\n"
        "/find <kata kunci> — cari prompt dan skill\n"
        "/paket <ID> — unduh petunjuk paket\n"
        "/alur — unduh demo alur kerja akademik"
    )


async def pencarian(pesan: Message, command: CommandObject) -> None:
    kata = (command.args or "").strip()
    if not kata:
        await pesan.answer("Cara menggunakan: /find <kata-kunci>")
        return
    ditemukan = search_catalogue(load_catalogue(), kata)[:5]
    if not ditemukan:
        await pesan.answer("Belum ada paket yang sesuai. Tanyakan pada teman atau usulkan kontribusi baru.")
        return
    await pesan.answer("Paket yang ditemukan:\n" + "\n".join(
        f'{p["id"]}: {p["name"]} [{STATUS.get(p["status"], p["status"])}]' for p in ditemukan
    ))


async def paket(pesan: Message, command: CommandObject) -> None:
    kode = (command.args or "").strip().casefold()
    if not kode:
        await pesan.answer("Cara menggunakan: /paket ST-02")
        return
    item = next((p for p in load_catalogue() if p["id"].casefold() == kode), None)
    if not item or not item["content"].strip():
        await pesan.answer("Petunjuk paket tidak ditemukan. Gunakan /find untuk mencari ID paket.")
        return
    status = STATUS.get(item["status"], item["status"])
    await pesan.answer_document(
        BufferedInputFile(item["content"].encode("utf-8"), filename=f'{item["id"]}.md'),
        caption=f'{item["id"]} · {item["name"]}\nStatus: {status}\nSumber: {item["path"]}',
    )


async def alur(pesan: Message) -> None:
    await pesan.answer_document(
        BufferedInputFile(DEMO.read_bytes(), filename=DEMO.name),
        caption="Demo Bayes dengan data sintetis. Sumber: 04-alur-kerja/DEMO_TERINTEGRASI.md",
    )


def buat_dispatcher() -> Dispatcher:
    async def grup_sesuai(pesan: Message) -> bool:
        diizinkan = pesan.chat.type in {"group", "supergroup"}
        if not diizinkan:
            LOGGER.warning("Pesan Telegram diabaikan karena berasal dari luar grup.")
        return diizinkan

    dp = Dispatcher()
    router = Router()
    router.message.filter(grup_sesuai)
    router.message.register(bantuan, Command("start", "help", "bantuan"))
    router.message.register(pencarian, Command("find"))
    router.message.register(paket, Command("paket"))
    router.message.register(alur, Command("alur"))
    dp.include_router(router)
    return dp


async def main() -> None:
    load_dotenv(AKAR / ".env")
    token = os.getenv("TELEGRAM_BOT_TOKEN_CI", "").strip()
    if not token:
        raise SystemExit("Isi TELEGRAM_BOT_TOKEN_CI terlebih dahulu.")
    dp = buat_dispatcher()
    async with Bot(token) as bot:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
