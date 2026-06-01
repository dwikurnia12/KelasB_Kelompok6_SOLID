from hewan.hewan import Hewan

class HewanDarat(Hewan):
    def __init__(self, nama: str, jenis: str):
        super().__init__(nama, jenis)

    def berjalan(self):
        print(f"{self.nama} sedang berjalan di darat.")
