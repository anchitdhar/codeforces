def calc(arr):
    for i in arr:
        for j in range(1,i):
            z = max(arr[i][j] - arr[j][i])
    print(z)
            


if __name__=="__main__":
    N = int(input())
    arr=[]
    for i in range(N):
        x = input().split(" ")
        arr.append(x)
    calc(arr)
