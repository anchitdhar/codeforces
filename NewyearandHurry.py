a, b = map(int,input().split(" "))
totalTime = 320
remaining_time = 320 - b
summofnum = 0
result = 1
for n in range(1, 100):
    z = n
    while int(result) > 0:
        result = min(int(remaining_time)/max(z*z+1))
print(result)