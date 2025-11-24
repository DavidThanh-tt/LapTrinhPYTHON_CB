while True:
    try:
        n = int(input('Nhập n > 0: '))
        if n > 0:
            break
    except:
        print('Ko đc nhập chữ')

i = 1
dem = 0
while i <= n:
    if i % 3 == 0:
        dem+=1
    i+=1
print(f'Có {dem} số chia hết cho 3')