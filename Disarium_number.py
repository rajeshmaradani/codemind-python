n=int(input())
m=len(str(n))
s=0
t=n
while n:
    r=n%10
    s+=r**m
    n//=10
    m-=1
if s==t:
    print("True")
else:
    print("False")