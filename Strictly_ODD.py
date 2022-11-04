n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(len(x)):
    if x[i]%2==1:
        if i%2==0:
            c+=1
            break
if c==1:
    print("False")
else:
    print("True")