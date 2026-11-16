# Arsitektur Awal

```text
Mahasiswa / Reviewer
        |
        +-- GitHub: berkas Markdown, YAML, contoh, hasil uji
        |
        +-- Streamlit: katalog dan pencarian
                  |
                  +-- modul kipp/catalog.py
                          |
                          +-- 02-prompt/ dan 03-skill/

Telegram (opsional) --> Bot perintah --> Pencarian katalog

Pengembangan berikutnya:
Bot Telegram --> layanan Python --> indeks pengetahuan --> Ollama lokal
                                     |
                                tinjauan manusia
```

Repositori Git adalah sumber utama paket terkurasi. Aplikasi Streamlit membaca berkas lokal. PostgreSQL, pgvector, dan Ollama adalah pilihan peningkatan setelah dasar komunitas dan pengujian berhasil.

Tab **Alur kerja akademik** membaca demo Markdown dari `04-alur-kerja/`. Paket prompt dan skill tetap dibaca lewat metadata YAML yang sama.

## Batasan keamanan

Bot katalog memproses perintah dari grup dan supergrup yang menambahkannya. Pertahankan pengaturan privasi Telegram dan minta persetujuan peserta sebelum mengaktifkan pemantauan percakapan. Jangan mengirim identitas atau isi forum ke model cloud tanpa izin.

## Rancangan uji integrasi lokal

1. Uji layanan Ollama secara terpisah menggunakan pertanyaan sintetis dan berkas katalog yang telah diizinkan sebagai sumber. Cantumkan ID dan jalur sumber pada jawaban serta tandai ketidakpastian saat bukti katalog kurang.
2. Sebelum uji di Telegram, sepakati tujuan, kelompok yang diizinkan, penggunaan data, dan persetujuan peserta. Uji dengan perintah eksplisit di grup yang ditetapkan.
3. Uji penolakan untuk grup lain, sumber kosong, dan Ollama yang gagal merespons. Pertahankan fungsi pencarian katalog saat model lokal gagal.
4. Ulas jawaban AI sebelum menjadikannya materi terverifikasi. Penggunaan riwayat forum untuk rangkuman memerlukan rancangan dan persetujuan tersendiri.
