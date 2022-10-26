def rev(n):
    rem=0
    while n:
        r=n%10
        rem=rem*10+r
        n=n//10
    return rem
n=int(input())
m=n**2
r1=rev(n)
r2=r1**2
r3=rev(r2)
if m==r3:
    print("True")
else:
    print("False")