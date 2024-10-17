target =[]

def lcm(a,b):
    for i in range(1, min(a,b) + 1):
        if a * i in target:
            return a * i
        target.append(i*b)
    return 0


a, b = map(int, input().split())

print(lcm(a,b))