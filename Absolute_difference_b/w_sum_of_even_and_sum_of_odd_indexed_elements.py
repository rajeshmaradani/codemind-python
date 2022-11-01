n=int(input())
arr=list(map(int,input().split()))
e=[]
o=[]
for i in range(n):
    if i%2==0:
        e.append(arr[i])
    else:
        o.append(arr[i])
p=sum(e)
q=sum(o)
print(abs(p-q))