class Santri:
    def __init__(self,nama,hujroh,kelas,pangkat,nilai,penjara):
        self.nama = nama
        self.hujroh = hujroh
        self.kelas = kelas
        self.pangkat = pangkat
        self.nilai = nilai
        self.penjara = penjara
    def hafal_quran(self):
        if self.nilai == 100:
            return True
        else:
            return False
    def anak_soleh(self):
        print("Insyaallah Sholeh")