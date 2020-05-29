n, h = input().split(" ")
arr = list(map(int, input().split(" ")))
count = 0
for i in range(len(arr)):
    if arr[i] <= int(h):
        count += 1
    else:
        count += 2
print(count)