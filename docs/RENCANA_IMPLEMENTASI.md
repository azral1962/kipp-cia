# Rencana Implementasi untuk Codex

## Tahap 1: pustaka dan katalog (prioritas utama)

1. Pastikan berkas metadata valid dan dibaca katalog.
2. Tersedia satu prompt draf per domain dan satu skill draf per kategori. Uji silang dan pengisian katalog rancangan masih tertunda.
3. Pertahankan pengujian otomatis dan dokumentasikan cara menjalankannya.
4. Filter status dan tag tersedia. Filter sumber serta dokumentasi hasil ulasan masih dijadwalkan.

## Tahap 2: pengalaman kolaborasi

1. Perbaiki template kontribusi dan pull request.
2. Tambahkan contoh kasus lintas mata kuliah dan tautan ke konsep.
3. Buat tampilan pengguna untuk membaca serta menyalin prompt dan skill.
4. Jalankan uji kemudahan penggunaan bersama mahasiswa lain.

## Tahap 3: forum dan AI lokal (opsional)

1. Terima perintah pengguna dari grup dan supergrup yang menambahkan bot.
2. Tambahkan `/ask` dan `/summary` hanya setelah ada rancangan privasi, sumber RAG, dan pengujian.
3. Sambungkan Ollama melalui antarmuka layanan terpisah.
4. Review manusia wajib sebelum menerbitkan materi menjadi pengetahuan terverifikasi.

Uji layanan Ollama dengan data sintetis secara lokal sebelum menyambungkannya ke bot. Tetapkan pemberitahuan bagi peserta, persetujuan, kelompok yang diizinkan, sumber katalog yang boleh dipakai, dan prosedur pemeriksaan manusia sebelum menguji dengan materi forum.

Tiap tahap: spesifikasi → implementasi → tes → review → dokumentasi → persetujuan.
