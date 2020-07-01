import random

n = 100
while(n != 10**8):
    z = 0
    i = n
    while i!=0:
        if random.randint(1,6) != 6:
            pass
        else:
            z = z + 1
        i = i - 1
    print(n,z)
    n = n * 10
print ("Good bye!")
#while双层循环不要用同一个判断变量