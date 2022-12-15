def count(s):
    c=0
    for i in s:
        if i in "aeiouAEIOU":
            c+=1
    return c
s=input()
s1=s.split()
r=[]
for i in s1:
    r.append(count(i))
print(*r)