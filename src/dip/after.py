from abc import ABC, abstractmethod

class hewan(ABC):

    @abstractmethod
    def makan(self):
        pass

class hewanterbang(hewan):

    @abstractmethod
    def terbang(self):
        pass

class kandang(ABC):

    @abstractmethod
    def tambah_hewan(self, hewan: hewan):
        pass

    @abstractmethod
    def get_semua_hewan(self):
        pass

    @abstractmethod
    def bersihkan(self):
        pass

class singa(hewan):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} (singa) sedang makan daging")

class elang(hewanterbang):
    def __init__(self, nama):
        self.nama = nama
    
    def makan(self):
        print(f"{self.nama} (elang) sedang makan ikan")

    def terbang(self):
        print(f"{self.nama} (elang) sedang terbang tinggi")

class kandang(kandang):
    def __init__(self):
        self._hewan_list = []

    def tambah_hewan(self, hewan: hewan):
        self._hewan_list.append(hewan)
    
    def get_semua_hewan(self):
        return self._hewan_list
    
    def bersihkan(self):
        print("Kandang biasa sedang dibersihkan")

class kandangVIP(kandang):

    def __init__(self):
        self._hewan_list = []
    
    def tambah_hewan(self, hewan: hewan):
       self._hewan_list.append(hewan)
    
    def get_semua_hewan(self):
        return self._hewan_list
    
    def bersihkan(self):
        print("Kandang VIP sedang dibersihkan dengan cairan pembersih")

class KebunBinatang:
    def __init__(self, kandang: kandang):  
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()
            
            if isinstance(hewan, hewanterbang):
                hewan.terbang()

kandang_biasa = kandang()
kandang_biasa.tambah_hewan(singa("Simba"))
kandang_biasa.tambah_hewan(elang("Raja"))

kebun1 = KebunBinatang(kandang_biasa)
print("=== Kebun Binatang dengan Kandang Biasa ===")
kebun1.rawat_semua_hewan()

print()
kandang_vip = kandangVIP()
kandang_vip.tambah_hewan(elang("Garuda"))

kebun2 = KebunBinatang(kandang_vip)  
print("=== Kebun Binatang dengan Kandang VIP ===")
kebun2.rawat_semua_hewan()