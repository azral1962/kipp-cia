# Bot Telegram KIPP-CIA

Bot katalog melayani perintah di semua grup dan supergrup yang menambahkannya. Bot mengabaikan chat pribadi dan menampilkan peringatan umum di konsol tanpa mencatat isi pesan atau identitas pengirim.

| Perintah | Hasil |
|---|---|
| `/start`, `/help`, `/bantuan` | Menampilkan daftar perintah. |
| `/find bayes` | Menemukan hingga lima paket prompt dan skill beserta statusnya. |
| `/paket ST-02` | Mengirim petunjuk Markdown paket, status, dan lokasi sumbernya. |
| `/alur` | Mengirim demo akademik Bayes dengan data sintetis. |

## Menjalankan

1. Pasang dependensi dengan `pip install -e '.[bot]'`.
2. Siapkan `.env` di akar KIPP-CIA berdasarkan `.env.example` dan isi `TELEGRAM_BOT_TOKEN_CI`.
3. Pertahankan pengaturan privasi grup di BotFather. Setelah konfigurasi forum disetujui, jalankan `python cia.py` dari akar KIPP-CIA.

Untuk mengganti bot forum lama pada akun Telegram yang sama, hentikan proses `ci.py` lama sebelum menyalakan `cia.py`. Jalankan satu proses polling per token. Fungsi forum lama seperti pencatatan pesan, refleksi, fasilitasi, dan konsensus tidak dipindahkan ke bot katalog. Bot katalog memakai berkas proyek lokal dan tidak mengakses basis data forum, daftar peserta, atau Ollama.
