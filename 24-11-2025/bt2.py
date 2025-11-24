while True:
    try:
        n = int(input('Nhập n > 0: '))
        if n > 0:
            break
    except ValueError:
        print('Ko đc nhập chữ')

i = 1
tong = 0
while i <= n:
    if i % 2 == 1:
        tong += i
    i += 1

print(f'Tổng: {tong}')