def isSHH(x):
    tongUoc = 0
    for i in range(1, x):
        if x % i == 0:
            tongUoc += i
    if tongUoc == x:
        print(f'{x}la so hoan hao')
    else:
        print(f'{x}ko phai la so hoan hao')        