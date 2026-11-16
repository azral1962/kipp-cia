"""Antarmuka awal katalog KIPP-CIA, seluruh pesan berbahasa Indonesia."""
from pathlib import Path
import sys
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kipp.catalog import AKAR, catalogue_tags, load_catalogue, search_catalogue  # noqa: E402

st.set_page_config(page_title="KIPP-CIA · Pustaka Akademik", page_icon="📚", layout="wide")
st.title("KIPP — Kecerdasan Akademik Kolektif")
paket = load_catalogue()
kategori = sorted({p["category"] for p in paket})
terjemahan_status = {"draft": "draf", "in_review": "dalam tinjauan", "beta": "beta", "verified": "terverifikasi", "deprecated": "tidak dianjurkan"}
tag_tersedia = sorted({tag for p in paket for tag in catalogue_tags(p)})
status_tersedia = sorted({p["status"] for p in paket})
tab_paket, tab_alur = st.tabs(["Prompt dan skill", "Alur kerja akademik"])

with tab_paket:
    st.caption("Paket berstatus draf menunggu pemeriksaan independen.")
    cari = st.text_input("Cari prompt atau skill", placeholder="Misalnya: Tutor Sokratik")
    kolom_kategori, kolom_status, kolom_tag = st.columns(3)
    pilihan = kolom_kategori.selectbox("Kategori", ["semua", *kategori])
    status = kolom_status.selectbox(
        "Status", [None, *status_tersedia],
        format_func=lambda nilai: "semua" if nilai is None else terjemahan_status.get(nilai, nilai),
    )
    tag = kolom_tag.selectbox("Tag", [None, *tag_tersedia], format_func=lambda nilai: "semua" if nilai is None else nilai)
    hasil = search_catalogue(paket, cari, pilihan, status=status, tag=tag)

    k1, k2, k3 = st.columns(3)
    k1.metric("Jumlah paket", len(paket))
    k2.metric("Hasil pencarian", len(hasil))
    k3.metric("Paket terverifikasi", sum(p["status"] == "verified" for p in paket))
    if not hasil:
        st.info("Tidak ada paket yang cocok dengan pencarian dan filter.")

    for item in hasil:
        with st.expander(f'{item["id"]} · {item["name"]} — {terjemahan_status.get(item["status"], item["status"])}'):
            st.write(item["description"])
            st.caption(f'{item["kind"]} · {item["category"]} · versi {item.get("version", "?")} · {item["path"]}')
            st.markdown(item["content"])

with tab_alur:
    demo = AKAR / "04-alur-kerja" / "DEMO_TERINTEGRASI.md"
    st.markdown(demo.read_text(encoding="utf-8"))
    st.caption(str(demo.relative_to(AKAR)))

st.divider()
st.markdown("**Ingin berkontribusi?** Pilih GitHub Issue, gunakan templat, ajukan pull request, lalu minta ulasan tim lain.")
st.markdown("Baca `CONTRIBUTING.md`, `00-proyek/piagam-proyek.md`, dan `docs/DAFTAR_TUGAS.md`.")
