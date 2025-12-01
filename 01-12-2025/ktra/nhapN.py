def nhapN():
    while True:
        try:
            n = int(input('Nhap so: '))
            if n > 0:
                return n
        except ValueError:
            print ('Nhap sai kieu du lieu!')    