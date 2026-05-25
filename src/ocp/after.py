from abc import ABC, abstractmethod

# Class induk diabstraksikan agar Open for Extension
class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

    @abstractmethod
    def bergerak(self):
        pass

# Mengembangkan jenis hewan baru tanpa mengubah class utama
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

# Class KebunBinatang menjadi Closed for Modification
class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.bergerak() # Polimorfisme secara otomatis memanggil cara bergerak tiap hewan