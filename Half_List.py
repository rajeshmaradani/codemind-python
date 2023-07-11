n=int(input())
a=list(map(int,input().split()))
e=n//2
s1=a[e:]
s2=s1[::-1]
s3=a[:e]
s=s2+s3
print(*s)