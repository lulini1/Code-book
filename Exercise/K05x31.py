n = int(input())
i=n
alist=[i]
while i!=1:
    if i%2==0:
        i=i // 2
    else:
        i=i * 3 + 1
    alist.append(int(i))

print(alist,len(alist))