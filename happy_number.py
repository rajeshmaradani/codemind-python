n=int(input())
sum=0
while n>9:
    while n:
        r=n%10
        sum+=r**2
        n=n//10
    n=sum
    sum=0
if n==1 or n==7:
    print("True")
else:
    print("False")