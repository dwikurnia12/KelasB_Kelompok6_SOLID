from hewan.hewan import Hewan
from habitat.kandang import Kandang
from zoo.kebun_binatang import KebunBinatang

elang = Hewan("Elang", "Burung")
simba = Hewan("Simba", "Singa")
nemo  = Hewan("Nemo", "Ikan")

kandang_burung = Kandang("Kandang Burung")
kandang_darat  = Kandang("Kandang Darat")
kandang_air    = Kandang("Kandang Air")

kandang_burung.tambah_hewan(elang)
kandang_darat.tambah_hewan(simba)
kandang_air.tambah_hewan(nemo)

kebun = KebunBinatang("Kebun Binatang SOLID")

kebun.tambah_kandang(kandang_burung)
kebun.tambah_kandang(kandang_darat)
kebun.tambah_kandang(kandang_air)

kebun.info()
kebun.beri_makan_semua()
kebun.rawat_semua_hewan()
