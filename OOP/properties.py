class SieuNhan:
    suc_manh = 50
    so_thu_tu = 1

    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1

    def xin_chao(self):
        print(f"Xin chao, ta la {self.ten}")
        print(f"Suc manh cua ta la {self.suc_manh}")


sieu_nhan_A = SieuNhan('Sieu nhan A', 'Sung', 'Do')
sieu_nhan_B = SieuNhan('Sieu nhan B', 'Kiem', 'Xanh')
sieu_nhan_c = SieuNhan('Sieu nhan C', 'Cung Ten', 'Vang')
print(SieuNhan.suc_manh)
print(sieu_nhan_A.suc_manh)

SieuNhan.suc_manh = 40

print(SieuNhan.suc_manh)
print(sieu_nhan_A.suc_manh)

print(sieu_nhan_A.stt)
print(sieu_nhan_B.stt)
print(sieu_nhan_c.stt)

sieu_nhan_A.xin_chao()
