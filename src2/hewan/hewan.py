from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama: str, jenis: str):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} ({self.jenis}) sedang makan.")
