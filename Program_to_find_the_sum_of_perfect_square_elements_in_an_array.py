import math
def sq(n):
    n1=int(math.sqrt(n))
    if n1*n1 == n:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if sq(i) == 1:
        s+=i
print(s)
