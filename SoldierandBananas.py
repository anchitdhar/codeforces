a = input().split(" ")
cost = int(a[0])
money = int(a[1])
want = int(a[2])
total = 0
for i in range(1, want + 1):
    total += i * cost

if (total - money) <= 0:
    print("0")
else:
    print(total-money)