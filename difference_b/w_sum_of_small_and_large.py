def count(s):
    r=[]
    r1=0
    r2=[0 for i in range(len(s))]
    m=0
    m1=0
    for i in s:
        r.append(ord(i))
    m+=min(r)
    m1+=max(r)
    return m1-m
s=input()
s=s.split()
r=[]
for i in s:
  r.append(count(i))
print(sum(r))