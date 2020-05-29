a = str(input())
a = a.replace("+", "")
arr = []
for i in range(len(a)):
    arr.append(int(a[i]))
arr.sort()
arr2 = []
for i in arr:
    arr2.append(str(i))
z = "+".join(arr2)
print(z)

