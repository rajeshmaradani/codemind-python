n=int(input())
x=list(map(int,input().split()))
m=int(input())
p=x.count(m)
if p>=1:
    print("True")
else:
    print("False")