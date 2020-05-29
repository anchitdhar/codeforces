a = int(input())
count = 0
arr =[]
for i in range(1,6):
    while a%i != 0:
        a = int(a / i)
        count += 1
    arr.append(count)
print(min(arr))
    