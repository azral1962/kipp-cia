# Demonstrasi Alur Kerja Akademik

**Kasus:** menjelaskan penggunaan Teorema Bayes pada klasifikasi spam.

1. **Belajar:** gunakan ST-02 untuk memahami konsep.
2. **Riset:** bandingkan sumber yang benar-benar tersedia.
3. **Desain:** tetapkan kriteria dan rancangan eksperimen.
4. **Implementasi:** buat kode Python dan uji terhadap acuan.
5. **Karya ilmiah:** susun klaim, bukti, grafik dan laporan.
6. **Komunikasi publik:** buat presentasi dan video penjelasan.

## Latihan dengan data sintetis

Gunakan 100 pesan rekaan. Dari 20 pesan spam, 10 mengandung kata «promo». Dari 80 pesan lainnya, 8 mengandung kata itu.

| Tahap | Hasil yang diserahkan | Pemeriksaan sejawat |
|---|---|---|
| Belajar | Penjelasan probabilitas bersyarat dengan bantuan ST-02 | Mahasiswa menjelaskan perbedaan antara peluang spam jika ada kata «promo» dan peluang munculnya kata itu pada pesan spam. |
| Riset | Catatan sumber dan asumsi | Gunakan konsep Bayes di `01-pengetahuan/konsep/contoh-bayes.md` sebagai titik awal dan catat sumber kuliah yang benar-benar dibaca. |
| Desain | Tabel frekuensi dan definisi kejadian | Periksa kembali label spam, kata yang dicari, dan jumlah setiap kelompok. |
| Implementasi | Perhitungan manual dan skrip Python, dengan PY-03 sebagai panduan pemeriksaan | Bandingkan hasil substitusi rumus Bayes dengan rasio langsung 10 dari 18 pesan berisi «promo». Keduanya harus menghasilkan sekitar 55,6%. |
| Karya ilmiah | Laporan singkat dengan tabel dan keterbatasan | Setiap klaim mengarah ke tabel atau sumber. Angka berlaku untuk data sintetis latihan ini. |
| Komunikasi publik | Presentasi atau video penjelasan | Seorang teman dapat menjelaskan kembali asal angka 55,6% dan keterbatasannya. |

Catat bantuan AI, koreksi manusia, dan keputusan reviewer sebelum membagikan hasil. Untuk tahap implementasi, periksa juga bagaimana skrip menangani kasus tanpa pesan yang mengandung kata «promo».

Cari paket pendamping di tab **Prompt dan skill** menggunakan ID berikut.

- Riset dan desain: `RS-03` dan `DS-02`.
- Implementasi dan bukti: `IM-05`, `PY-03`, `TB-01`, dan `VZ-01`.
- Pelaporan dan komunikasi: `PP-01`, `DC-01`, `SL-01`, dan `VD-01`.
