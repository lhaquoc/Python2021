# Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng.
def BT8():
    data = input('Nhập vào dãy số nguyên bất kỳ cách nhau bởi khoảng trắng:')
    nlist = data.split(' ')
    nlist_num = map(int, nlist)
    print(sum(nlist_num))

# Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng.
# có xử lý exception


def BT9():
    data = input('Nhập vào dãy số nguyên bất kỳ cách nhau bởi khoảng trắng:')
    nlist = data.split(' ')
    try:
        nlist_num = map(int, nlist)
        print(sum(nlist_num))
    except:
        print('Định dạng input không hợp lệ')

# Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output theo mẫu


def BT10():
    with open('BT10.in', 'r') as file_in:
        name = file_in.readline().rstrip('\n')
        tuoi = int(file_in.readline())

    with open('BT10.out', 'w') as file_out:
        file_out.write(f'Vào 20 năm nữa, tuổi của {name} sẽ là {tuoi + 20}')

    file_in.close()
    file_out.close()

# Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output theo mẫu
# có xử lý exception


def BT11():
    try:
        with open('BT10.in', 'r') as file_in:
            name = file_in.readline().rstrip('\n')
            tuoi = int(file_in.readline())

        with open('BT10.out', 'w') as file_out:
            file_out.write(f'Vào 20 năm nữa, tuổi của {name} sẽ là {tuoi + 20}')

        file_in.close()
        file_out.close()
    except FileNotFoundError:
        with open('BT10.out', 'w') as file_out:
            file_out.write('Không tìm thấy file input.')
    except:
        with open('BT10.out', 'w') as file_out:
            file_out.write('Định dạng input không hợp lệ.')


def BT16():
    name_1, height_1 = input().split()
    name_2, height_2 = input().split()
    try:
        height_1 = int(height_1)
        height_2 = int(height_2)
        if height_1 <= 0 or height_2 <= 0:
            print('Chieu cao phai lon hon 0')
            return -1
        if height_1 == height_2:
            print(f'{name_1} cao bang {name_2}')
        if height_1 > height_2:
            print(f'{name_1} cao hon {name_2}')
        if height_1 < height_2:
            print(f'{name_1} thap hon {name_2}')

    except:
        print('input khong hop le!')


def BT17():
    a, b, c = map(float, input().split())  # ham map se mang input dua vao ham float -> float number
    if a + b > c and a + c > b and b + c > a:
        print(f'{a}, {b}, {c} la ba canh cua mot tam giac.')
        return -1
    print(f'{a}, {b}, {c} khong la ba canh cua mot tam giac.')


def BT18():
    try:
        a, b, c = map(float, input().split())  # ham map se mang input dua vao ham float -> float number
        if a <= 0 or b <= 0 or c <= 0:
            print('Cac canh tam giac phai lon hon 0.')
            return -1
        if a + b > c and a + c > b and b + c > a:
            print(f'{a}, {b}, {c} la ba canh cua mot tam giac.')
            return -1
        print(f'{a}, {b}, {c} khong la ba canh cua mot tam giac.')
    except:
        print('Dinh dang input khong hop le.')


def main():
    # BT8()
    # BT9()
    # BT10()
    # BT16()
    # BT17()
    BT18()


if __name__ == '__main__':
    main()
