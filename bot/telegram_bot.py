"""Bot Telegram pilihan: hanya perintah, tanpa menyimpan pesan atau memakai LLM."""
from __future__ import annotations
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from kipp.catalog import load_catalogue, search_catalogue

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
GRUP_DIIZINKAN = {int(x.strip()) for x in os.getenv("TELEGRAM_ALLOWED_CHAT_IDS", "").split(",") if x.strip()}
dp = Dispatcher()


def diizinkan(pesan: Message) -> bool:
    return bool(GRUP_DIIZINKAN) and pesan.chat.id in GRUP_DIIZINKAN


@dp.message(Command("help"))
async def bantuan(pesan: Message) -> None:
    if diizinkan(pesan):
        await pesan.answer("Bot KIPP-CIA: gunakan /find <kata-kunci>. Pesan percakapan tidak disimpan.")


@dp.message(Command("find"))
async def pencarian(pesan: Message) -> None:
    if not diizinkan(pesan):
        return
    kata = (pesan.text or "").partition(" ")[2].strip()
    if not kata:
        await pesan.answer("Cara menggunakan: /find <kata-kunci>")
        return
    ditemukan = search_catalogue(load_catalogue(), kata)[:5]
    if not ditemukan:
        await pesan.answer("Belum ada paket yang sesuai. Tanyakan pada teman atau usulkan kontribusi baru.")
        return
    await pesan.answer("Paket yang ditemukan:\n" + "\n".join(
        f'{p["id"]}: {p["name"]} [{"draf" if p["status"] == "draft" else p["status"]}]' for p in ditemukan
    ))


async def main() -> None:
    if not TOKEN or not GRUP_DIIZINKAN:
        raise SystemExit("Isi TELEGRAM_BOT_TOKEN dan TELEGRAM_ALLOWED_CHAT_IDS terlebih dahulu.")
    async with Bot(TOKEN) as bot:
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
