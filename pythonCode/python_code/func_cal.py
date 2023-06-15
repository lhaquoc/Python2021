def input_user():
    # nhap vao so n tu ban phim
    return int(input("n:"))
def calc_n(n):
    # tinh bang cuu chuong n
    i = 2
    while i >= 2 and i < 10:
        print(f"{n} x {i} = {n * i}")
        i = i + 1
