class SieuNhan:
    suc_manh = 50

    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def xin_chao(self):
        print(f'Xin chao, ta la {self.ten}')

    def show_suc_manh(self):
        print(f'Suc manh cua ta la {self.suc_manh}')

    def __str__(self):
        return f'Day la {self.ten }, su dung {self.vu_khi}'

# tao class ke thua


class SieuNhanGao(SieuNhan):
    suc_manh = 55

    # def __init__(self, ten, vu_khi, mau_sac, sieu_thu):
    #     self.ten = ten
    #     self.vu_khi = vu_khi
    #     self.mau_sac = mau_sac
    #     self.sieu_thu = sieu_thu
    def __init__(self, ten, vu_khi, mau_sac, sieu_thu):
        super().__init__(ten, vu_khi, mau_sac)
        self.sieu_thu = sieu_thu

    def show_suc_manh(self):
        print(f'Suc manh cua ta la {self.suc_manh}')
        print(f'Sieu thu cua ta la {self.sieu_thu}')

    def __repr__(self):
        return f'ten: {self.ten}\nmau sac: {self.mau_sac}\nvu khi: {self.vu_khi}'


gao_xanh = SieuNhanGao("Gao xanh", "Ten lua", "Xanh", "Cho soi")
print(gao_xanh.__dict__)
print(gao_xanh.suc_manh)
gao_xanh.xin_chao()
gao_xanh.show_suc_manh()

print('%s' % gao_xanh)
print('%r' % gao_xanh)
