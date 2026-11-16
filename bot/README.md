# Bot Telegram — Versi Awal

Bot berbasis aiogram hanya melayani dua perintah: `/help` dan `/find kata-kunci`. Gunakan berkas `.env` lokal, berdasarkan `.env.example`, untuk membatasi ID grup dan menyimpan token.

Bot ini **tidak menyimpan percakapan** dan **belum terhubung dengan LLM**. Penambahan pemantauan grup memerlukan penjelasan, izin, retensi terbatas, dan verifikasi tersendiri.

Jalankan: `pip install -e '.[bot]'` lalu `python -m bot.telegram_bot`.
