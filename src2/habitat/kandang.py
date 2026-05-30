class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
        print(f"Berhasil memasukkan {hewan.nama} ke dalam kandang.")