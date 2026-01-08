for i in range(int(input())):
    arr = list(map(int,input().split()))
    
    for i in range(len(arr)):
        res=0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                res +=1
        if res==1:
            print(arr[i],end=" ")
    print()
    