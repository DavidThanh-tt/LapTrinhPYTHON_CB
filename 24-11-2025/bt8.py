while True:
    try:
        n = int(input("nhap n:"))
        if(n>0):
            break
    except ValueError:
        print("loi nhap sai du lieu.")
i = 1
max = -1000
min = 1000
while (i<=n):
    try:
        so = int(input(f"nhap so thu{i}:"))
        i+=1
        if(so>max):
            max = so
        if(so<min):
            min = so
    except ValueError:
        print("sai kieu du lieu.")
print(f"gia tri lon nhat la {max}, nho nhat la {min}")                                