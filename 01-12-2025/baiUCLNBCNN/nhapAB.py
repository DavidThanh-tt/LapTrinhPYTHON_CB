def nhapAB():
    while True:
        try: 
            A = int(input('Nhap A: '))
            B = int(input('Nhap B: '))
            if A > 0 and B > 0:
                return A,B
        except ValueError:
            print('Nhap sai kieu du lieu!')

