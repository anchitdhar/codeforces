N = int(input())
s = list(map(int,input().split(" ")))
count = 0
maxVal = s[0]
for i in range(len(s)):
    if s[i] >= s[0]:
        maxVal = s[i]
        count+=1

print(count)