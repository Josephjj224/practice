target =[]

def lcm(a,b):
    if a == b:
        return min(a,b)
    for i in range(1, max(a,b) +1):
        if a * i in target:
            return a * i
            break
        if b * i in target:
            return b * i
            break

        target.append(i*b)
        target.append(i*a)
    return -1


a, b = map(int, input().split())

print(lcm(a,b))