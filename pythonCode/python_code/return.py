def cal_rec_per(width, height):
    return (width+height)*2


def main():
    width = float(input('width:'))
    height = float(input('height:'))
    print(cal_rec_per(width, height))


if __name__ == '__main__':
    main()
