while True:
    try:
        n = int(input('Nhập n > 0: '))
        if n > 0:
            break
    except ValueError:
        print('Ko đc nhập chữ')

for i in range(1,11):
    print(f"Bảng cửu chương {n}")
    print(f'{i} x {n} = {i*n}\n')

