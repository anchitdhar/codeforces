a = str(input())
b = str(input())
a = a.lower()
b = b.lower()
last_a = a
last_b = b
if last_a > last_b:
    print("1")
elif last_a < last_b:
    print("-1")
else:
    print("0")