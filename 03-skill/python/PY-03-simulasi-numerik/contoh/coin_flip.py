"""Simulasi pelemparan koin dengan sumber acak yang dapat direproduksi."""
import random


def simulasi_koin(jumlah: int, benih: int = 42) -> float:
    """Mengembalikan proporsi sisi angka dari sejumlah lemparan."""
    if jumlah <= 0:
        raise ValueError("Jumlah lemparan harus positif")
    acak = random.Random(benih)
    return sum(acak.random() < 0.5 for _ in range(jumlah)) / jumlah


if __name__ == "__main__":
    print(f"Proporsi sisi angka: {simulasi_koin(10000):.4f}")
