n=int(input())
s = str(input())
a,d=0,0
for i in range(len(s)):
    if s[i] == "A":
        a += 1
    else:
        d += 1
if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")