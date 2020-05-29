N = int(input())
values = map(int,input().split(" "))
sum = 0
for i in values:
    sum = sum + i
    z = (sum) / N * 100
    
print(z / 100)