def solve(N):
    if N % 2 == 0:
        return int(N / 2)
    else:
        prev = (N - 1) / 2
        return int(prev-N)  

if __name__ == "__main__":
    print(solve(int(input())))