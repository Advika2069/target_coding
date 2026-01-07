arr = list(map(int,input().split()))
target = list(map(int,input().split()))
result = []
for x in target:
    found = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == x:
                found = True
                break
        if found:
            break
    result.append(found)
print(result)