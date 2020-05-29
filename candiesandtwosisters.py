arr = []
for _ in range(int(input())):
    x = input().split("\n")
    arr.append(x)

a = 2
b = 1
count = 0
for i in range(len(arr)):
    if arr[i] > 2:
        a = arr[i] - b
        while a > 0 and b > 0 and a + b == arr[i] and a > b:
            count += 1
        print("count")
    else:
        print("0")

// Doesnt work