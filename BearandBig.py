L, B = input().split(" ")
L = int(L)
B =int(B)
count = 0
while L <= B:
    L = 3 * L
    B = 2 * B
    count += 1
print(count)
