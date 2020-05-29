X = list(map(int,input().split(" ")))
M = -9999999
for i in X:
    if M > i:
        M = M
    else:
        M = i

arr = []
for i in X:
    if M - i != 0:
        arr.append(M - i)
for i in arr:
    print(i, end = " ")
        