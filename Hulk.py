def solve(n):
    for i in range(n):
        if i % 2 == 0:
            print("I hate",end=" ")
        else:
            print("I love",end=" ")
        if (i != n - 1):
            print("that",end=" ")
        else:
            print("it",end=" ")

if __name__ == "__main__":
    solve(int(input()))