from habitat.kandang import Kandang
from services.perawatan import Perawatan
from services.pemberian_makan import PemberianMakan

class KebunBinatang:
    def __init__(self, nama):
        self.nama = nama
        self.kandang_list = []

    def tambah_kandang(self, kandang: Kandang):
        self.kandang_list.append(kandang)
        print(f"Kandang '{kandang.nama_kandang}' ditambahkan ke {self.nama}.")

    def rawat_semua_hewan(self):
        print(f"\n--- Merawat semua hewan di {self.nama} ---")
        for kandang in self.kandang_list:
            for hewan in kandang.hewan_list:
                Perawatan.rawat(hewan)

    def beri_makan_semua(self):
        print(f"\n--- Memberi makan semua hewan di {self.nama} ---")
        for kandang in self.kandang_list:
            for hewan in kandang.hewan_list:
                PemberianMakan.beri_makan(hewan)

    def info(self):
        print(f"\n--- Info {self.nama} ---")
        for kandang in self.kandang_list:
            print(f"Kandang: {kandang.nama_kandang}")
            for hewan in kandang.hewan_list:
                print(f"  - {hewan.nama}")
