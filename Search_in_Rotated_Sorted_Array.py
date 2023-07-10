n=int(input())
l=list(map(int,input().split()))
c=0
k=int(input())
for i in range(len(l)):
    if l[i]==k:
        print(i)
        c=1
        break
if c==0:
    print(-1)
        