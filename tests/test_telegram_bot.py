"""Uji akses grup dan perintah katalog tanpa koneksi Telegram."""

import asyncio
from unittest.mock import AsyncMock

import pytest

pytest.importorskip("aiogram")
from aiogram import Bot
from aiogram.methods import SendDocument, SendMessage
from aiogram.types import Update

from bot.telegram_bot import buat_dispatcher


def test_perintah_katalog_dari_grup_dan_supergrup(monkeypatch, caplog):
    async def jalankan():
        dp = buat_dispatcher()
        async with Bot("123:token-sintetis") as bot:
            kirim = AsyncMock(return_value=True)
            monkeypatch.setattr(bot.session, "make_request", kirim)

            async def pesan(chat_id, jenis, teks):
                update = Update.model_validate({
                    "update_id": 1,
                    "message": {
                        "message_id": 1,
                        "date": 0,
                        "chat": {"id": chat_id, "type": jenis},
                        "text": teks,
                    },
                })
                await asyncio.wait_for(dp.feed_update(bot, update), timeout=2)

            await pesan(123, "private", "/paket ST-02")
            await pesan(-1001, "supergroup", "Teks percakapan sintetis")
            kirim.assert_not_awaited()
            assert [
                log.getMessage() for log in caplog.records if log.name == "bot.telegram_bot"
            ] == ["Pesan Telegram diabaikan karena berasal dari luar grup."]

            await pesan(-1001, "supergroup", "/find ST-02")
            await pesan(-1002, "group", "/paket st-02")
            await pesan(-1003, "supergroup", "/alur")
            hasil_cari, paket, alur = [panggilan.args[1] for panggilan in kirim.await_args_list]
            assert isinstance(hasil_cari, SendMessage) and "ST-02" in hasil_cari.text
            assert isinstance(paket, SendDocument) and paket.document.filename == "ST-02.md"
            assert isinstance(alur, SendDocument) and alur.document.filename == "DEMO_TERINTEGRASI.md"
            assert (hasil_cari.chat_id, paket.chat_id, alur.chat_id) == (-1001, -1002, -1003)

    asyncio.run(jalankan())
