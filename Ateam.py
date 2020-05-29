n = int(input())
arr = []
for i in range(n):
    arr.append(input())

z =['1 0 1','1 1 0','1 1 1','0 1 1']
count = 0
for i in arr:
    if i in z:
        count += 1
print(count)