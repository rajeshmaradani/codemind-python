def ispretty(n):
    d=n%10
    if d==2 or d==3 or d==9:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        if ispretty(j):
            c+=1
    print(c)