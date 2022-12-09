def polin(n):
    t=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if t==rev:
        return 1
    else:
        return 0
n=int(input())
d=[0]*n
for i in range(n):
    val=int(input())
    d[i]=val
for i in d:
    if polin(i)==1:
        print("True")
    else:
        print("False")