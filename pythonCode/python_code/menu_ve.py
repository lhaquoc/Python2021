import turtle
t = turtle.Pen()
def print_usage():
    print('nhap so 1 - ve hinh tron\n')
    print('nhap so 2 - ve hinh vuong\n')
    print('nhap so 3 - ve hinh ngoi sao\n')
    print('nhap so 0 - thoat chuong trinh\n')

def ve_hinh_tron(kich_thuoc):
        t.circle(kich_thuoc)
        
def ve_ngoi_sao(kich_thuoc):
    for x in range(5):
        t.forward(kich_thuoc)
        t.right(144)
        
def ve_hinh_vuong(kich_thuoc):
    for i in range(5):
        t.forward(kich_thuoc)
        t.right(90)
    
def check_input():
    while True:
        check = int(input('nhap so de chon mode:'))
        t.reset()
        if check == 0:
            break
        if check == 1:
            kich_thuoc = int(input('nhap kich thuoc:'))
            ve_hinh_tron(kich_thuoc)
        if check == 2:
            kich_thuoc = int(input('nhap kich thuoc:'))
            ve_hinh_vuong(kich_thuoc)
        if check == 3:
            kich_thuoc = int(input('nhap kich thuoc:'))
            ve_ngoi_sao(kich_thuoc)
    

def main():
    # thu tu hoat dong cua chuong trinh:
    # 1. huong dan su dung
    # 2. nguoi dung nhap so
    # 3. kiem tra so da nhap
    # 4. ve hinh theo so da nhap
    # 5. nguoi dung nhap so ( # 2.)
    print_usage()
    check_input()

if __name__ == '__main__':
    main()
