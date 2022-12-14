s=input()
e=[]
s=s.split()
for i in s:
    e.append(len(i))
print(max(e))