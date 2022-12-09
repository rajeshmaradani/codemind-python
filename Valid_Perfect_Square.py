import math
n=int(input())
d=[0]*n
for i in range(n):
    val=int(input())
    d[i]=val
for i in d:
    m=int(math.sqrt(i))
    if m*m==i:
        print("True")
    else:
        print("False")
    