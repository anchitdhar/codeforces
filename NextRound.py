n, k = map(int, input().split(" "))
arr = list(map(int,input().split(" ")))
count = 0
for i in arr:
    if (i > 0 and i >= arr[k-1]):
        count += 1

print(count)


