target =[]

def lcm(a,b):
    for i in range(1, 100):
        if a * i in target:
            return a * i
            break
        target.append(i*b)
    return 0


a, b = map(int, input().split())

print(lcm(a,b))