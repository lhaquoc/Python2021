class SieuNhan:
    suc_manh = 50

    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    @staticmethod
    def bien_hinh():
        print('1 2 3 bien hinh!')


sieu_nhan_a = SieuNhan('Sieu nhan do', 'Kiem', 'Do')
sieu_nhan_a.bien_hinh()
