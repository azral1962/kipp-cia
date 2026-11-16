Dalam proyek **KIPP-CIA (Collective Intelligence for Academics)**, sebuah prompt sebaiknya bukan sekadar pertanyaan kepada AI, melainkan **instruksi kerja terstruktur yang dapat digunakan berulang kali, diuji oleh mahasiswa lain, dan diperbaiki bersama**.

Saya berikan lima contoh prompt untuk pekerjaan akademik, lalu satu contoh format paket yang dapat disimpan dalam repository `kipp-cia`.

## **1. Contoh prompt untuk lima kegiatan akademik**

**ST-02 — Tutor Socrates untuk Memahami Konsep**

Tujuan: membantu mahasiswa memahami teori, bukan sekadar memperoleh jawaban.

Bertindaklah sebagai tutor yang membimbing saya memahami suatu konsep melalui dialog Socrates.

**Mata kuliah:** [nama mata kuliah]\
**Topik:** [konsep yang dipelajari]\
**Tujuan:** [kemampuan yang ingin dikuasai]

Lakukan langkah berikut:

1. Tanyakan apa yang sudah saya pahami.
2. Identifikasi pengetahuan prasyarat.
3. Ajukan satu pertanyaan pada setiap giliran.
4. Berikan petunjuk apabila saya kesulitan.
5. Jangan langsung memberikan jawaban lengkap.
6. Minta saya menjelaskan konsep menggunakan kata-kata sendiri.
7. Berikan satu persoalan baru untuk menguji kemampuan saya.

Di akhir pembelajaran, berikan umpan balik berdasarkan jawaban saya dan rekomendasikan langkah belajar berikutnya.

**RS-02 — Asisten Kajian Literatur**

Tujuan: membantu penelitian dan membandingkan temuan ilmiah.

Bertindaklah sebagai asisten penelitian.

**Topik:** [topik penelitian]\
**Pertanyaan penelitian:** [pertanyaan]\
**Lingkup:** [bidang, periode, dan batasan]

Bantu saya:

1. Mengidentifikasi konsep serta kata kunci pencarian.
2. Menyusun strategi penelusuran literatur.
3. Membandingkan metode, temuan, dan keterbatasan penelitian yang saya berikan.
4. Mengidentifikasi kesamaan, perbedaan, dan kemungkinan research gap.
5. Membuat matriks kajian literatur.

Jangan membuat referensi fiktif. Bedakan informasi yang telah diverifikasi dengan dugaan atau rekomendasi pencarian.

Keluaran: tabel literatur, sintesis temuan, dan pertanyaan penelitian lanjutan.

**DS-03 — Perancang Alternatif Solusi**

Tujuan: mengembangkan alternatif sebelum memutuskan desain.

Bertindaklah sebagai konsultan perancangan sistem.

**Masalah:** [deskripsi masalah]\
**Pengguna:** [siapa yang akan menggunakan solusi]\
**Sumber daya:** [waktu, biaya, teknologi, dan kemampuan]\
**Batasan:** [kendala yang harus dipenuhi]

Lakukan:

1. Rumuskan kembali masalah dan tujuan.
2. Identifikasi stakeholder dan kebutuhannya.
3. Kembangkan sedikitnya tiga alternatif solusi.
4. Bandingkan alternatif berdasarkan manfaat, kompleksitas, biaya, risiko, dan keberlanjutan.
5. Usulkan arsitektur solusi.
6. Jelaskan asumsi yang masih perlu diuji.

Jangan langsung menganggap alternatif pertama sebagai yang terbaik.

Keluaran: tabel alternatif, rekomendasi bersyarat, dan rancangan awal.

**IM-02 — Asisten Pemrograman Python**

Tujuan: membuat program yang dapat dipahami dan diuji.

Bertindaklah sebagai tutor dan software engineer Python.

**Persoalan:** [masalah yang ingin diselesaikan]\
**Input:** [data yang tersedia]\
**Output:** [hasil yang diharapkan]\
**Library:** [NumPy, Pandas, SciPy, Matplotlib, dan sebagainya]

Kerjakan secara bertahap:

1. Jelaskan model penyelesaian dan asumsi.
2. Susun algoritma atau pseudocode.
3. Buat program Python yang mudah dibaca.
4. Sertakan komentar pada bagian penting.
5. Buat pengujian untuk kondisi normal dan kasus ekstrem.
6. Jelaskan cara menjalankan program.
7. Interpretasikan hasil dan keterbatasannya.

Jangan mengklaim bahwa program telah diuji jika kode belum benar-benar dijalankan.

Keluaran: kode, panduan penggunaan, contoh hasil, dan pengujian.

**PP-02 — Penyusun Kerangka Paper Ilmiah**

Tujuan: membangun tulisan ilmiah dengan argumentasi yang runtut.

Bertindaklah sebagai pembimbing penulisan ilmiah.

**Judul sementara:** [judul]\
**Masalah penelitian:** [masalah]\
**Tujuan:** [tujuan penelitian]\
**Metode:** [metode yang digunakan]\
**Hasil yang tersedia:** [data atau temuan]

Bantu saya:

1. Merumuskan kontribusi utama paper.
2. Menyusun struktur IMRaD.
3. Membuat outline setiap bagian.
4. Menuliskan topic sentence untuk setiap paragraf utama.
5. Mengusulkan tabel dan gambar beserta caption.
6. Memeriksa hubungan antara klaim dan bukti.
7. Mengidentifikasi kekurangan data dan argumentasi.

Jangan membuat hasil eksperimen atau referensi yang tidak tersedia.

Keluaran: outline lengkap, daftar kebutuhan bukti, dan rencana penulisan.

## **2. Contoh prompt untuk menggunakan skill**

Prompt berikut menggabungkan kemampuan teknis AI dengan pekerjaan akademik.

**VZ-01 — Visualisasi Ilmiah**

Buat visualisasi ilmiah berdasarkan data atau model yang saya berikan.

**Data/model:** [data atau persamaan]\
**Variabel independen:** [nama dan satuan]\
**Variabel dependen:** [nama dan satuan]\
**Tujuan grafik:** [apa yang hendak dijelaskan]

Pilih jenis grafik yang sesuai, buat label sumbu dan legenda, serta tampilkan satuan yang benar.

Jika menggunakan Python Matplotlib, sertakan source code yang dapat dijalankan. Jangan mengarang nilai data.

Jelaskan tiga kesimpulan utama yang benar-benar didukung grafik.

**SL-01 — Presentasi Akademik**

Buat rancangan presentasi akademik berdasarkan materi berikut:

**Topik:** [topik]\
**Audiens:** [sasaran]\
**Durasi:** [menit]\
**Pesan utama:** [pesan]

Susun alur presentasi menggunakan TAIDA:\
Target, Attention, Interest, Desire, Action.

Untuk setiap slide, berikan judul yang menyampaikan pesan, poin utama, usulan visual, dan catatan pembicara.

Utamakan visual yang mendukung pemahaman dan hindari slide yang terlalu padat teks.

Jangan memasukkan klaim tanpa bukti.

**VD-01 — Video Penjelasan Konsep**

Rancang video edukasi berdurasi 60–90 detik.

**Konsep:** [topik]\
**Penonton:** [sasaran]\
**Tujuan belajar:** [kemampuan yang diharapkan]

Buat:

1. Kalimat pembuka yang menarik perhatian.
2. Penjelasan masalah atau kebutuhan.
3. Storyboard per adegan beserta durasi.
4. Narasi atau voice-over.
5. Deskripsi visual, animasi, atau demonstrasi.
6. Penutup yang merangkum konsep.
7. Daftar aset yang perlu dibuat.

Pastikan klaim ilmiah akurat dan durasi total sesuai permintaan.

## **3. Format paket prompt untuk repository&#x20;**`kipp-cia`

Setiap tim sebaiknya menyimpan prompt dalam folder yang mempunyai struktur standar:

```
02-prompt/
└── belajar/
    └── ST-02-tutor-socrates/
        ├── README.md
        ├── prompt.md
        ├── metadata.yaml
        ├── contoh/
        │   ├── probabilitas.md
        │   └── sinyal-sistem.md
        ├── pengujian/
        │   └── hasil-uji.md
        └── RIWAYAT-PERUBAHAN.md
```

Misalnya `README.md` menjelaskan tujuan dan kapan prompt digunakan, `prompt.md` berisi instruksi siap pakai, `metadata.yaml` mencatat versi serta kontributor, sedangkan folder `pengujian` menyimpan hasil yang diperiksa mahasiswa lain.

## **4. Bagaimana mahasiswa menguji kualitas prompt?**

Saya menyarankan lima kriteria berikut, masing-masing bernilai 0–5.

**Simulasi evaluasi prompt**

# **19/25**

Contoh nilai reviewer

Kejelasan instruksi

4/5

Tujuan, konteks, dan keluaran jelas

Ketepatan hasil

3/5

Kebenaran jawaban dan bukti pendukung

Kemudahan penggunaan

4/5

Dapat digunakan mahasiswa lain

Transferabilitas

4/5

Dapat diterapkan lintas mata kuliah

Manfaat pembelajaran

4/5

Meningkatkan pemahaman dan kemandirian

Penilaian sebaiknya dilengkapi komentar kualitatif dan bukti pengujian. Satu nilai tinggi tidak otomatis menjamin prompt benar untuk semua kasus.

## **5. Tugas sederhana untuk setiap mahasiswa**

Untuk memulai proyek, saya menyarankan setiap mahasiswa melakukan satu kegiatan:

**Pilih satu persoalan akademik nyata yang sedang Anda hadapi. Buat atau gunakan satu prompt untuk membantunya. Uji hasilnya, diskusikan dengan teman, perbaiki prompt, lalu dokumentasikan pengalaman tersebut.**

Contoh yang dapat dipilih adalah memahami materi yang sulit, membuat program Python, mengolah data, merancang presentasi, atau memperbaiki tulisan ilmiah.

Hasil akhirnya bukan hanya sebuah prompt, melainkan:

**Masalah → Prompt → Respons AI → Pemeriksaan → Umpan balik teman → Revisi → Pengetahuan bersama.**

Inilah pola kolaborasi yang ingin kita budayakan melalui KIPP-CIA, sehingga pada semester berikutnya mahasiswa dapat menggunakan metode yang sama untuk bidang ilmu yang berbeda.