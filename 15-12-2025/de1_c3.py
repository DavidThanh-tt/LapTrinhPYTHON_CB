#Cau 3
Diem = [7.5, 8.0, 6.0, 9.0, 5.5, 8.5, 7.0, 6.5]
#a. Tinh diem trung binh
tong = 0
for value in Diem:
    tong += value
Diem_TB = tong/len(Diem)
print (f"Diem trung binh la: {Diem_TB}")
#b. Tim diem cao nhat
max = Diem[0]
for value in Diem:
    if value > max:
        max = value
print(f"Diem cao nhat la: {max}")
#c. Dem so diem >=8.0 & <8.0
lon_hon_8 = 0
nho_hon_8 = 0
for value in Diem:
    if value >= 8.0:
        lon_hon_8 += 1
    else:
        nho_hon_8 += 1
print(f"So diem >= 8.0: {lon_hon_8}")
print(f"So diem < 8.0: {nho_hon_8}")
#d. Sap xep ds tang dan
for i in range(len(Diem)-1):
    for j in range(i + 1, len(Diem)):
        if(Diem[i] > Diem[j]):
            Diem[i],Diem[j] = Diem[j], Diem[i]
print("Danh sach tang dan:", Diem)            
