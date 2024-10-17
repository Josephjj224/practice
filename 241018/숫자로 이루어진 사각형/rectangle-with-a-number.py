a = input()

h_count = 1
v_count = 1
num_count = 1
while(v_count <= int(a)):
    if h_count <= int(a):
        print(num_count, end=' ')
        num_count += 1
        h_count += 1
    else: 
        print()
        v_count += 1
        h_count = 1
    if num_count >= 10:
        num_count = 1