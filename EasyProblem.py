N = int(input())
a = map(int, input().split(" "))
arr = []
for i in a:
    if i == 0:
        arr.append("EASY")
    else:
        arr.append("HARD")

if "HARD" in arr:
    print("HARD")
else:
    print("EASY")