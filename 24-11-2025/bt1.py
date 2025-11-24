while True:
    try:
        n = int(input('Nhập n > 0: '))
        if n > 0:
            break
    except:
        print('Ko đc nhập chữ')

i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i+=1