N = int(input())
arr =[]
for i in range(1, N):
    arr[1][i] = 1
    
    for i in range(2,N):
        for j in range(1,N):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
            
print(arr)