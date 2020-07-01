import random

#n = int(input("please input n:"))
n = 60000
z = 0
while n!=0:
    if random.randint(1,6) != 6:
        pass
    else:
        z = z + 1
    n = n - 1
print(z)

#import math
#p = z/n
#print(p)