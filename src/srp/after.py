from abc import ABC, abstractmethod

class DapatMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class DapatTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class Burung(DapatMakan, DapatTerbang):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} (Burung) sedang makan biji-bijian.")

    def terbang(self):
        print(f"{self.nama} (Burung) sedang terbang tinggi.")

class Singa(DapatMakan): 
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} (Singa) sedang makan daging.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: DapatMakan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang: Kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            if isinstance(hewan, DapatTerbang):
                hewan.terbang()