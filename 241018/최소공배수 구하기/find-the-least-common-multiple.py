target =[]

def lcm(a,b):
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0: 
            target.append(i)
    return max(target)* max(target)


a, b = map(int, input().split())

print(lcm(a,b))