n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if i%2==0:
        c+=1
if c==n:
    print("True")
else:
    print("False")