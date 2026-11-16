"""Merender Markdown proyek menjadi situs Quarto dengan indeks di akar."""
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory


AKAR = Path(__file__).resolve().parents[2]
WEB = Path("dokumentasi-web")
KELOMPOK = {
    "": "Panduan utama",
    "00-proyek": "Organisasi proyek",
    "01-pengetahuan": "Pengetahuan",
    "02-prompt": "Pustaka prompt",
    "03-skill": "Pustaka skill",
    "04-alur-kerja": "Alur kerja akademik",
    "05-pemecahan-masalah": "Pemecahan masalah",
    "06-contoh": "Contoh lintas mata kuliah",
    "07-komunitas": "Komunitas dan ulasan sejawat",
    "08-aplikasi": "Aplikasi katalog",
    "09-mutu": "Pengujian dan mutu",
    "10-pameran-karya": "Pameran karya",
    "docs": "Spesifikasi pengembang",
    "bot": "Bot Telegram",
    "templat": "Templat kontribusi",
    ".github": "Kontribusi melalui GitHub",
}
ARSIP_LOKAL = {"_site", "_freeze", "node_modules", "__pycache__", WEB.name}


def daftar_markdown():
    """Menemukan dokumen proyek, termasuk templat GitHub yang tersembunyi."""
    for folder, direktori, berkas in os.walk(AKAR):
        induk = Path(folder).relative_to(AKAR)
        direktori[:] = sorted(
            nama for nama in direktori
            if (nama == ".github" and induk == Path("."))
            or (
                not nama.startswith(".")
                and nama not in ARSIP_LOKAL
                and induk / nama not in {Path("data/pribadi"), Path("data/rahasia")}
                and not (Path(folder) / nama / "pyvenv.cfg").is_file()
            )
        )
        for nama in sorted(berkas):
            path = Path(folder) / nama
            if path.suffix.lower() == ".md" and not nama.startswith(".") and not path.is_symlink():
                yield path.relative_to(AKAR)


def siapkan_halaman(sumber, proyek):
    teks = (AKAR / sumber).read_text(encoding="utf-8-sig")
    metadata = re.match(r"\A---\n(.*?)\n---\n", teks, re.DOTALL)
    isi = teks[metadata.end():] if metadata else teks
    heading = re.match(r"\A\s*# (.+)\n", isi)
    nama = re.search(r"^name:\s*(.+)$", metadata[1], re.MULTILINE) if metadata else None
    judul = heading[1] if heading else nama[1] if nama else sumber.stem
    if heading:
        isi = isi[heading.end():]

    jalur = sumber.as_posix()
    tujuan = WEB / jalur.removeprefix(".") if jalur.startswith(".github/") else WEB / sumber
    tujuan = tujuan.with_suffix(".qmd")
    if tujuan.name.casefold() == "readme.qmd":
        tujuan = tujuan.with_name("README.md.qmd")
    halaman = proyek / tujuan
    halaman.parent.mkdir(parents=True, exist_ok=True)
    halaman.write_text(
        f"---\ntitle: {json.dumps(judul, ensure_ascii=False)}\n---\n\n"
        f"Sumber: `{jalur}`\n\n{isi}",
        encoding="utf-8",
    )
    return tujuan, judul


def main():
    sumber = sorted(daftar_markdown())
    kelompok = {nama: [] for nama in KELOMPOK}
    with TemporaryDirectory(prefix="kipp-quarto-") as folder:
        proyek = Path(folder)
        shutil.copy2(AKAR / "_quarto.yml", proyek)
        indeks = [
            "---\ntitle: \"Dokumentasi KIPP-CIA\"\n---",
            f"Jelajahi {len(sumber)} dokumen proyek menurut bagian. "
            "Gunakan pencarian di bilah navigasi untuk menemukan isi dokumen.",
        ]
        halaman_dokumen = []
        for path in sumber:
            tujuan, judul = siapkan_halaman(path, proyek)
            halaman_dokumen.append(tujuan.with_suffix(".html"))
            grup = path.parts[0] if len(path.parts) > 1 else ""
            kelompok.setdefault(grup, []).append(
                f"- [{escape(judul).replace('[', '&#91;').replace(']', '&#93;')}](<{tujuan.as_posix()}>) · `{path.as_posix()}`"
            )
        for grup, tautan in kelompok.items():
            if tautan:
                indeks.append("\n".join([f"## {KELOMPOK.get(grup, grup)}", "", *tautan]))
        (proyek / "index.qmd").write_text("\n\n".join(indeks) + "\n", encoding="utf-8")

        try:
            subprocess.run(["quarto", "render"], cwd=proyek, check=True)
        except FileNotFoundError:
            raise SystemExit("Perintah quarto belum tersedia. Pasang Quarto CLI terlebih dahulu.") from None

        hasil = proyek / "_site"
        for halaman in halaman_dokumen:
            if not (hasil / halaman).is_file():
                raise SystemExit(f"Hasil render tidak ditemukan untuk {halaman}.")
        shutil.copytree(hasil / WEB, AKAR / WEB, dirs_exist_ok=True)
        for nama in ("index.html", "search.json"):
            shutil.copy2(hasil / nama, AKAR / nama)
    print(f"Dokumentasi {len(sumber)} berkas tersedia di {AKAR / 'index.html'}.")


if __name__ == "__main__":
    main()
