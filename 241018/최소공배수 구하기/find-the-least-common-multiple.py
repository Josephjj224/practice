target =[]

def lcm(a,b):
    if a == b:
        return min(a,b)
    for i in range(1, max(a,b) +1):
        if a * i in target:
            return a * i
            break
        target.append(i*b)
    return 


a, b = map(int, input().split())

print(lcm(a,b))