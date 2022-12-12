n=int(input())
d=[0]*n
for i in range(0,n):
    a,b=map(int,input().split())
    d[i]=a+b
for i in d:
    print(i)