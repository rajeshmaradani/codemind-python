for i in range(int(input())):
    m,n=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in b:
        a.append(i)
    print(*sorted(a))