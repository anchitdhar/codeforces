N = int(input())
s = str(input())
s =s.lower()
arr = []
if N < 26:
    print("NO")
else:
    dic = {x: s.count(x) for x in s}
    for key in dic.keys():
        arr.append(key)
    if len(arr) == 26:
        print("YES")
    else:
        print("NO")