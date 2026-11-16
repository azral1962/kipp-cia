"""Membaca dan menelusuri katalog prompt serta skill dari berkas YAML."""
from __future__ import annotations
from pathlib import Path
import yaml

AKAR = Path(__file__).resolve().parents[1]
DIREKTORI = ("02-prompt", "03-skill")
KOLOM_WAJIB = {"id", "name", "category", "status", "description"}


def load_catalogue(root: Path = AKAR) -> list[dict]:
    """Membaca metadata; data tidak lengkap akan memunculkan kesalahan yang jelas."""
    hasil: list[dict] = []
    for direktori in DIREKTORI:
        for path in sorted((root / direktori).rglob("metadata.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            if not isinstance(data, dict) or not KOLOM_WAJIB.issubset(data):
                raise ValueError(f"Metadata tidak lengkap: {path}")
            item = dict(data)
            item["kind"] = "Prompt" if direktori == "02-prompt" else "Skill"
            item["path"] = str(path.parent.relative_to(root))
            calon = [path.parent / "prompt.md", path.parent / "SKILL.md", path.parent / "README.md"]
            pratinjau = next((p for p in calon if p.exists()), None)
            item["content"] = pratinjau.read_text(encoding="utf-8") if pratinjau else ""
            hasil.append(item)
    return hasil


def search_catalogue(
    items: list[dict],
    query: str = "",
    category: str = "semua",
    *,
    status: str | None = None,
    tag: str | None = None,
) -> list[dict]:
    """Menyaring katalog berdasarkan istilah, kategori, status, dan tag."""
    kata = query.casefold().strip()
    cocok = []
    for item in items:
        if category not in ("semua", "all") and item.get("category") != category:
            continue
        if status is not None and item.get("status") != status:
            continue
        if tag is not None and tag not in catalogue_tags(item):
            continue
        teks = " ".join(str(item.get(k, "")) for k in ("id", "name", "description", "category", "tags"))
        if kata in teks.casefold():
            cocok.append(item)
    return cocok


def catalogue_tags(item: dict) -> list[str]:
    """Mengambil tag yang dapat ditampilkan dari metadata opsional."""
    tags = item.get("tags")
    if isinstance(tags, str):
        return [tags] if tags.strip() else []
    if isinstance(tags, list):
        return [tag for tag in tags if isinstance(tag, str) and tag.strip()]
    return []
