"""Uji katalog berkas lokal."""
from kipp.catalog import load_catalogue, search_catalogue, AKAR


def test_memuat_contoh():
    paket = load_catalogue()
    assert {"ST-02", "PY-03"}.issubset({x["id"] for x in paket})
    assert {x["category"] for x in paket if x["kind"] == "Prompt"} >= {
        "belajar", "riset", "desain", "implementasi", "karya-ilmiah",
    }
    assert {x["category"] for x in paket if x["kind"] == "Skill"} >= {
        "python", "visualisasi", "tabel", "presentasi", "video", "dokumen",
    }
    assert all(x["content"].strip() for x in paket)


def test_pencarian_kode_kategori():
    paket = load_catalogue()
    cocok = search_catalogue(paket, "ST-02", "belajar")
    assert len(cocok) == 1
    assert cocok[0]["name"] == "Tutor Sokratik"
    assert search_catalogue(paket, "ST-02", "python") == []


def test_lokasi_sumber_ada():
    for item in load_catalogue():
        assert (AKAR / item["path"]).is_dir()


def test_filter_status_dan_tag_dapat_digabung():
    paket = [
        {"id": "A", "category": "belajar", "status": "draft", "tags": ["dialog"]},
        {"id": "ST-99", "category": "belajar", "status": "verified", "tags": ["dialog"]},
        {"id": "C", "category": "belajar", "status": "draft", "tags": ["dialogis"]},
        {"id": "D", "category": "belajar", "status": "draft"},
    ]

    assert search_catalogue(paket, category="belajar", status="draft", tag="dialog") == [paket[0]]
    assert search_catalogue(paket, "ST-99", status="draft", tag="dialog") == []
    assert search_catalogue(paket, category="semua") == paket
