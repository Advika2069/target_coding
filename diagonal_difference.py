n = int(input())
arr = []
right = 0
left = 0
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
for i in range(n):
    right += arr[i][i]
    left+=arr[i][n-1-i]
print(abs(right-left))
