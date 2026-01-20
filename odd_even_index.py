s = input()
o = []
e = []
for i in range(len(s)):
    if i%2==0:
        e.append(s[i])
    else:
        o.append(s[i])
eresult = ''.join(e)
oresult = ''.join(o)
print(eresult+oresult)
