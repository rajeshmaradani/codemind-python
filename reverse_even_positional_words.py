s=input()
s1=s.split()
n=len(s1)
for i in range(n):
    if i%2==0:
        print(s1[i][::-1],end=" ")
    else:
        print(s1[i],end=" ")