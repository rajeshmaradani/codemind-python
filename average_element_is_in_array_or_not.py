n=int(input())
x=list(map(int,input().split()))
m=sum(x)//n
p=x.count(m)
if p>=1:
    print("True")
else:
    print("False")