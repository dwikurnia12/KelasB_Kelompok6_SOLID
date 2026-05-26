from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

class HewanTerbang(Hewan):
    @abstractmethod
    def terbang(self):
        pass

class BurungMerpati(HewanTerbang):
    def makan(self):
        print(f"{self.nama} makan biji-bijian.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Singa(Hewan):  
    def makan(self):
        print(f"{self.nama} makan daging.")
