n=int(input())
m=n*n
length=len(str(n))
last=m%pow(10,length)
if(last==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")