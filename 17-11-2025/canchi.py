try:
    namDL = int(input("Nhap nam duong lich: "))

except:
    print ("Loi cu phap!")

else:
    duCan = namDL % 10
    duChi = namDL % 12
    can = ''
    chi =''
    match duCan:
        case 0: can = 'canh'
        case 1: can = 'tan'
        case 2: can = 'nham'
        case 3: can = 'quy'
        case 4: can = 'giap'
        case 5: can = 'at'
        case 6: can = 'binh'
        case 7: can = 'dinh'
        case 8: can = 'mau'
        case 9: can = 'ky'

    match duChi:
        case 0: chi = 'than'
        case 1: chi = 'dau'
        case 2: chi = 'tuat'
        case 3: chi = 'hoi'
        case 4: chi = 'ti'
        case 5: chi = 'suu'
        case 6: chi = 'dan'
        case 7: chi = 'meo'
        case 8: chi = 'thin'
        case 9: chi = 'ty'    
        case 10: chi = 'ngo'
        case 11: chi = 'mui'

    print(can,chi)    




