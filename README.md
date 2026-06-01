# Zoo Management System- Analisis Prinsip SOLID

## Deskripsi Tugas
Project ini merupakan implementasi konsepm Pemrograman Berorientasi Object menggunakan bahasa Python dengan menerapkan prinsip- pinsip SOLID. Sistem dibuat dengan studi kasus manajemen kebun binatang yang terdiri dari pengelolaan hewan, habitat, layanan perawatan, serta kemampuan khusus hewan melalui interface.


## Pembagian Tugas
| No | Nama | NIM | Bagian Project |
|----|------|-----|---------------|
| 1  | Diah Anggraeni | K3525055 | class hewan |
| 2  | Arofa Karindra Bimantara       | K3525051 | class habitat |       
| 3  | Febriana Putri Qurata'ayun       | K3525007 | class services |
| 4  | Queennera Martha Kusuma W       | K3525012 | class zoo + main.py |
| 5  | Dwi Kurniawati Hanifah       | K3525056 | class interface |

## Studi kasus

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()        

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()

## Struktur Repository

```text
src2/
├── habitat/
│   └── kandang.py
├── hewan/
│   ├── hewan.py
│   ├── hewan_darat.py
│   └── hewan_terbang.py
├── interface/
│   ├── bisa_berenang.py
│   └── bisa_terbang.py
├── services/
│   ├── pemberian_makan.py
│   └── perawatan.py
├── zoo/
│   └── kebun_binatang.py
└── main.py
