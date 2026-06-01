from hewan.hewan import Hewan
class HewanTerbang(Hewan):
    def __init__(self, nama: str, jenis: str):
        super().__init__(nama, jenis)

    def terbang(self):
        print(f"{self.nama} sedang terbang di angkasa.")
