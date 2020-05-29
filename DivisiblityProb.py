N = int(input())
count = 0
arr = list(map(int, input().split(" "), input().split()))

for i in range(N):
    while arr[i][0] % arr[i][1] != 0:
        arr[i][0] = arr[i][0] + 1
        count += 1
    print(count)
    count = 0
