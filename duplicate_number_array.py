#find duplicate number in array 
for i in range(int(input())):
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        found = False
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                found = True
                break 
        if found:
            if i==0 or arr[i] != arr[i-1]:
                print(arr[i])
    


