n=int(input())
c=0
p=1
t=n
while n:
    p=1
    r=n%10
    for i in range(1,r+1):
        p=p*i
    n=n//10
    c=c+p
if c==t:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")
    