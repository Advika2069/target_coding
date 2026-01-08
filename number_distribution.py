#count occurence of positive,negative and zeroes in the given array.
for i in range(int(input())):
    arr = list(map(int,input().split()))
    pos = 0 
    neg = 0
    zero = 0 
    for i in arr:
        if i>0:
            pos+=1 
        elif i<0:
            neg+=1 
        else:
            zero+=1
    print(pos,neg,zero)