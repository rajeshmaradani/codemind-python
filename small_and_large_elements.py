s=input()
s1=s.split()
r=[]
r1=[]
m=s1[0]
m1=s1[len(s1)-1]
for i in m:
    r.append(ord(i))
for i in m1:
    r1.append(ord(i))
m2=min(r)
m3=max(r1)
print(chr(m2),chr(m3))