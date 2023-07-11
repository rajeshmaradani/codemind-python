for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    start=0
    c=0
    s=0
    for i in range(len(a)):
        s+=a[i]
        if k==0:
            print(0)
            break
        while s>k:
            s-=a[start]
            start+=1
        if s==k:
            print(start+1,i+1)
            c=1
            break
    if c==0:
        print(-1)