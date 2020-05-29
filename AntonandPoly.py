n = int(input())
name = []
for i in range(n):
    x = str(input())
    name.append(x)

sum = 0

for i in name:
    if i == "Tetrahedron":
        sum += 4
    elif i == "Cube":
        sum += 6
    elif i == "Octahedron":
        sum += 8
    elif i == "Dodecahedron":
        sum += 12
    else:
        sum += 20

print(sum)