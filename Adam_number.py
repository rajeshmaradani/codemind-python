def rev(n):
    t=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev    


n=int(input())
m=n*n
o=rev(n)
q=o*o
p=rev(q)
if p==m:
    print("True")
else:
    print("False")

