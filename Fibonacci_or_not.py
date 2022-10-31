n=int(input())
a=0
b=1
c=0
s=0
while n>=c:
    if c==n:
        s+=1
        break
    c=a+b
    a=b
    b=c
if s==1:
    print("True")
else:
    print("False")
    
    