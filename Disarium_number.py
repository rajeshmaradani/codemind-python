n=int(input())
l=len(str(n))
s=0
t=n
while n:
    r=n%10
    s=s+r**l
    n=n//10
    l-=1
if t==s:
    print("True")
else:
    print("False")