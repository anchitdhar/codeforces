s = list(map(int, input().split(" ")))
count = 0
s = sorted(s)
for i in range(0,len(s)-1):
    if s[i] == s[i + 1]:
        count += 1
    
print(count)
