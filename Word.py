s = str(input())
upper = 0
lower =0
for i in range(len(s)):
    if s[i] >= "A" and s[i] <= "Z":
        upper += 1
    else:
        lower += 1
    
if upper > lower:
    print(s.upper())
elif upper < lower:
    print(s.lower())
else:
    print(s.lower())
