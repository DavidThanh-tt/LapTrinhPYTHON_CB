try:
    van = float(input("nhap diem van:"))
    toan = float(input("nhap diem toan:"))
    anh = float(input("nhap diem anh:"))
except ValueError:
    print("loi sai kieu du lieu!")
else:
    tb = (van + toan + anh)/3
    if van < 0 or van > 10 or toan < 0 or toan > 10 or anh < 0 or anh > 10:
        print('nhap diem khong hop le')
    else:
        if (tb >= 9):
            print("xep loai xuat sac")
        elif (tb >= 8):
            print ("xep loai gioi")
        elif (tb >= 7):
            print ("xep loai kha")
        elif (tb >= 5):
            print ("xep loai TB")
        else:
            print ("xep loai yeu")       
                     