arr =[]
for i in range(int(input())):
    x = str(input())
    arr.append(x)
count = 1
if len(arr) == 0:
    PRINT("0")
else:
    for _ in range(0,len(arr)-1):
        if arr[_] != arr[_ + 1]:
            count += 1
        
print(count)