dk = True
while dk:
    try:
        N = int(input("nhap N:"))
        if N > 0:
            break
    except ValueError:
        print ("loi nhap du lieu!")
i = 1
while i <= N:
    print(i, end=" ")
    i += 1
