n=int(input())
t=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if(t==sum):
    print("True")
else:
    print("False")