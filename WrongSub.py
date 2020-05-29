n, k = input().split(" ")
for i in range(len(k)):
    while i in int(k):
        if int(n) % 10 != 0:
            n =int(n) - 1
        else:
            n = int(n) / 10
            n = int(n)
print(n)