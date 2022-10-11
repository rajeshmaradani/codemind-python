n=int(input())
total=0
condition = True

while condition:

    while n :
        total+=n%10
        n//=10    
    n=total
    total=0
    condition=n>9
print(n)