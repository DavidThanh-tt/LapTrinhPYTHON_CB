def nhap_chuoi():
    str_input = input("Nhap chuoi: ")
    return str_input

def dodaichuoi(str):
    print(f"Chieu dai cua {str}: {len(str)}")

def first_char(str):
    print(f"Ky tu dau tien {str}: {str[0]}")

def mid_char(str):
    mid_index = len(str) // 2
    print(f"Ky tu giua {str}: {str[mid_index]}")

def last_char(str):
    print(f"Ky tu cuoi cung {str}: {str[-1]}")   

def cat_chuoi(str):
    print("Ba ky tu dau:", str[:3])
    print("Ba ky tu cuoi:", str[-3:]) 

def hoa_thuong(str):
    print("Viet hoa", str.upper())
    print("Viet thuong", str.lower())

def noi_chuoi(ho, ten_dem, ten):
    str = ho + " " + ten_dem + " " + ten
    print("Ho ten day du:", str)                     