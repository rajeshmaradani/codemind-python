def count(s):
    c=0
    for i in s:
        if i in "aeiouAEIOU":
            c+=1
    return c
s=input()
s1=s.split()
r=[]
c=0
for i in s1:
    r.append(count(i))
r1=min(r)
for i in r:
    if i==r1:
        c+=1
print(c)