n=int(input())
a=list(map(int,input().split()))
s=''
for i in a:
    s+=str(i)
k=int(s)+1
n1=str(k)
n2=[]
for i in n1:
    n2.append(int(i))
print(*n2)
    