def nhapCdCr():
    while True:
        try: 
            cd = int(input('Nhap chieu dai: '))
            cr = int(input('Nhap chieu rong: '))
            if cd > 0 and cr > 0:
                return cd,cr
        except ValueError:
            print('Nhap sai kieu du lieu!')



def tinhcvdt(cd,cr):
    dt = cd*cr
    cv = (cd+cr)*2
    return cv,dt

CdCr = nhapCdCr()
CvDt = tinhcvdt(CdCr[0],CdCr[1])
print(f'Chu vi HCN: {CvDt[0]}')
print(f'Dien tich HCN: {CvDt[1]}')

