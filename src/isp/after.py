from abc import ABC, abstractmethod

class IBisaMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class IBisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class IBisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

class Burung(IBisaMakan, IBisaTerbang):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Singa(IBisaMakan):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan.")
        
