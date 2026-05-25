class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()