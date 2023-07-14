for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    e=[]
    for i in range(n//2):
        e.append(max(a))
        e.append(min(a))
        a.remove(max(a))
        a.remove(min(a))
    for i in a:
        e.append(i)
    print(*e)
        