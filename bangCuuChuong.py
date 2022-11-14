''' tinh bang cuu chuong 2'''
def tinhCuuChuong(j):
    for i in range(1, 11):
        print(f'{j} x {i} = {j*i}')
        # pfrint(f'3 x {i} = {3*i}')

def tinhCuuChuongTuADenB():
    a = int(input('nhap a:'))
    b = int(input('nhap b:'))
    for j in range(a, b):
        tinhCuuChuong(j)
#tinhCuuChuongTuADenB()
tinhCuuChuong(j=3)
tinhCuuChuong(4)
tinhCuuChuong(5)
tinhCuuChuong(7)
tinhCuuChuong(9)

