"""Uji contoh simulasi koin."""
import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "03-skill/python/PY-03-simulasi-numerik/contoh/coin_flip.py"
spec = importlib.util.spec_from_file_location("simulasi_koin", PATH)
modul = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul)


def test_acak_dapat_diulang():
    assert modul.simulasi_koin(1000, 7) == modul.simulasi_koin(1000, 7)


def test_hasil_antara_nol_dan_satu():
    assert 0 <= modul.simulasi_koin(100) <= 1


def test_jumlah_invalid():
    with pytest.raises(ValueError):
        modul.simulasi_koin(0)
