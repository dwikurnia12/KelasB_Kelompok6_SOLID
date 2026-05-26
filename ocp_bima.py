# BIMA GACOR
from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

    @abstractmethod
    def bergerak(self):
        pass


class Burung(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")
    
    def bergerak(self):
        print(f"{self.nama} sedang terbang.")


class Singa(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")
    
    def bergerak(self):
        print(f"{self.nama} sedang berlari.")


class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self, hewan_list):
        for hewan in hewan_list:
            hewan.makan()
            hewan.bergerak()