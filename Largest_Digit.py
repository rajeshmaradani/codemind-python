n=int(input())
z=len(str(n))
y=0
for i in range(z):
    if(n%10>y):
        y=n%10
        n//=10
    else:
        n//=10
print(y)