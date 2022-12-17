s=input()
c=0
for i in s:
    j=ord(i)
    if j>64 and j<91:
        c+=1
print(c)