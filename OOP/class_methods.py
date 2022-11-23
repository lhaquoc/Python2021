class SieuNhan:
    suc_manh = 50

    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    @classmethod
    def cap_nhat_suc_manh(cls, suc_manh):
        cls.suc_manh = suc_manh

    @classmethod
    def from_string(cls, str):
        lst = str.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)


# sieu_nhan_A = SieuNhan('Sieu nhan do', 'Kiem', 'Do')

# print(SieuNhan.suc_manh)
# print(sieu_nhan_A.suc_manh)
# SieuNhan.cap_nhat_suc_manh(40)
# print(SieuNhan.suc_manh)
# print(sieu_nhan_A.suc_manh)
info_str = "Sieu nhan do - Kiem - Do"
sieu_nhan_a = SieuNhan.from_string(info_str)
print(sieu_nhan_a.__dict__)
