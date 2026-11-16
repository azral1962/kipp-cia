# KIPP-CIA — Kecerdasan Akademik Kolektif

**Satu kelas · 60+ mahasiswa · tiga minggu · sumber belajar bersama untuk semester berikutnya.**

Repositori awal proyek mata kuliah **Komunikasi Interpersonal dan Publik (KIPP)**. Mahasiswa mengembangkan pustaka **prompt, skill, alur kerja, konsep, dan pengalaman pemecahan masalah** yang dapat diuji, ditinjau, digunakan ulang, serta dikembangkan lintas mata kuliah.

## Mulai cepat

Persyaratan: Python 3.11 atau lebih baru dan Git.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
streamlit run app/streamlit_app.py
```

Di tab **Prompt dan skill**, gunakan kolom pencarian dan gabungkan filter kategori, status, dan tag. Tab **Alur kerja akademik** memuat latihan Bayes yang dapat diikuti kelompok dengan data sintetis.

Jalankan pengujian:

```bash
pytest -q
```

## Situs dokumentasi Quarto

Buka `index.html` di akar repositori untuk menjelajahi dokumen Markdown proyek. Untuk merender ulang setelah mengubah atau menambahkan Markdown, jalankan dari akar repositori dengan Python dan Quarto CLI terpasang.

```bash
python3 08-aplikasi/skrip/bangun_dokumentasi.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Buka `http://127.0.0.1:8000/` agar pencarian Quarto berfungsi. Simpan `index.html`, `search.json`, dan folder `dokumentasi-web/` bersama-sama. Lingkungan virtual, konfigurasi tersembunyi lokal, dan direktori data pribadi dikecualikan dari pemindaian.

Bot Telegram katalog (opsional):

```bash
pip install -e '.[bot]'
cp .env.example .env
# isi TELEGRAM_BOT_TOKEN_CI di .env
python cia.py
```

Bot merespons perintah di grup dan supergrup yang menambahkannya. Lihat `bot/README.md` untuk daftar perintah dan prosedur perpindahan dari bot forum lama.

## Peta repositori

- `00-proyek/`: piagam proyek, pembagian tim, jadwal, penilaian.
- `01-pengetahuan/`: taksonomi dan konsep.
- `02-prompt/`: lima domain kerja akademik.
- `03-skill/`: enam kategori keterampilan AI.
- `04-alur-kerja/`: proses akademik yang dapat digunakan ulang.
- `05-pemecahan-masalah/`: kasus, solusi, refleksi.
- `06-contoh/`: penerapan lintas mata kuliah.
- `07-komunitas/`: aturan, diskusi, dan ulasan sejawat.
- `08-aplikasi/`: rancangan pengembangan aplikasi.
- `09-mutu/`: rubrik, kasus uji, hasil verifikasi.
- `10-pameran-karya/`: demonstrasi dan hasil akhir.
- `app/`: antarmuka Streamlit.
- `bot/`: bot Telegram tahap awal.
- `kipp/`: pustaka Python untuk katalog.
- `templat/`: formulir kontribusi.
- `docs/`: spesifikasi untuk pengembang/Codex.

## Mulai berkontribusi

Baca `CONTRIBUTING.md` lalu ambil tugas melalui GitHub Issues, buat cabang, lengkapi templat, ajukan pull request, dan minta ulasan tim lain.

Dokumen prioritas: `AGENTS.md`, `docs/KONTEKS_PROYEK.md`, `docs/KEBUTUHAN.md`, dan `docs/RENCANA_IMPLEMENTASI.md`.

**Bahasa kerja:** Bahasa Indonesia untuk dokumentasi, UI, pesan bot, dan contoh. Nama perintah, library, ekstensi, API, serta kunci metadata teknis tetap menggunakan ejaan yang diperlukan perangkat lunak.
