class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.gerbong = ""
        self.jumlah_kursi = 0
        self.jenis_layanan_kereta = ""
        self.rute = []

    def tambah_rute(self, rute):
        self.rute.append(rute)

    def kurangi_rute(self, rute):
        if rute in self.rute:
            self.rute.remove(rute)

class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_mobil = jenis_mobil

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.front_wing = ""
        self.rear_wing = ""

    def race(self):
        print(f"{self.nama} sedang berlomba!")

class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.sunroof_type = ""
        self.shock_breaker = ""

    def sunroof_terbuka(self):
        print(f"Sunroof pada {self.nama} terbuka.")

    def sunroof_tertutup(self):
        print(f"Sunroof pada {self.nama} tertutup.")
