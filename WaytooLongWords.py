n = int(input())
arr = []
for i in range(n):
    arr.append(input())
for i in arr:
    if len(i) > 10:
        print(i[0] + str(len(i) - 2) + i[-1])
    else:
        print(i)