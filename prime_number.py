n=int(input())
c=0
if n==1:
    print("not a prime")
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        c+=1
        break
if c==0:
    print("prime")
else:
    print("not a prime")