# Pedoman untuk Agen Pengembang — kipp-cia

Anda membantu proyek kelas **KIPP Collective Academic Intelligence** dengan **Bahasa Indonesia sebagai bahasa utama**. Semua penjelasan, komentar yang berguna bagi mahasiswa, UI, template, pesan kesalahan, dokumentasi, issue, dan laporan harus berbahasa Indonesia. Simbol Python, nama dependensi, sintaks Git, format metadata, dan API tidak boleh diterjemahkan jika merusak kompatibilitas.

## Tujuan dan batas

- Target MVP tiga minggu bagi sekitar 60 mahasiswa, terbagi menjadi 10 tim.
- Pustaka 25 rancangan pola prompt (minimal 10 teruji), 15 rancangan skill (minimal 6 teruji), contoh alur akademik terintegrasi, katalog yang dapat digunakan dan sistem ulasan sejawat.
- Komponen bot Telegram hanyalah kerangka pilihan; **jangan membaca/menyimpan pesan tanpa persetujuan dan konfigurasi eksplisit**.
- Utamakan keterampilan komunikasi, kontribusi komunitas, pemeriksaan manusia, dan sumber yang dapat dilacak.
- Jangan mengubah model data atau membuat integrasi layanan berbayar tanpa persetujuan pemilik proyek.

## Cara bekerja

1. Baca `README.md`, `docs/KONTEKS_PROYEK.md`, `docs/KEBUTUHAN.md`, `docs/ARSITEKTUR.md`, dan `docs/RENCANA_IMPLEMENTASI.md`.
2. Kerjakan satu fitur kecil dalam satu perubahan: spesifikasi → implementasi → pengujian → dokumentasi → tinjauan.
3. Gunakan `pytest -q` sebelum mengklaim selesai. Jangan mengaku sudah menguji bila belum.
4. Jaga kompatibilitas pembaca katalog dan YAML; kunci metadata teknis seperti `id`, `name`, `category`, `status` tidak diganti sembarangan.
5. Hindari data pribadi asli di repositori dan log. Jangan memasukkan token ke kode.
6. Setiap saran AI yang bersifat ilmiah harus menyediakan sumber atau menandai ketidakpastian.
7. Jelaskan setiap perubahan dan risiko dalam bahasa Indonesia.

## Larangan tanpa persetujuan

- Mempublikasikan isi diskusi Telegram atau identitas mahasiswa.
- Mengirim data komunitas ke model eksternal.
- Menghapus data atau melakukan deployment produksi.
- Menganggap output AI otomatis tervalidasi.
