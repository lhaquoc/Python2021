a=int(input('nhap so a:')) #string->int
b=int(input('nhap so b:')) #string->int

my_list_a = list(range(a,b+1))

for i in range(0, 3): #(i=0, check i < 3), i tang theo thu tu 0,1,2,3,4,5,......
    print(my_list_a[i])
