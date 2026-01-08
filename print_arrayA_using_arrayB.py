n = int(input())
arrA = list(map(int,input().split()))
m = int(input())
arrB = list(map(int,input().split()))
for i in range(m):
    if 0<=arrB[i]<n:
        print(arrA[arrB[i]],end=" ")
    else:
        print(-1,end=" ")
    