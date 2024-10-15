def star(col, row):
    for i in range(col):
        print('1'*row)

a, b = map(int, input().split())


star(a,b)