n=int(input())
flag=0
while n>0:
    if n%5==0:
        n=n/5
        flag=1
    if n%2==0:
        n=n/2
        flag=1
    if n%3==0:
        n=n/3
        flag=1
    if n==1 or flag==0:
        break
if n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
    