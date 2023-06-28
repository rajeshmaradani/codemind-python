
s=input()
c=0
for i in s:
    if ord(i)>48 and ord(i)<58:
        c+=int(i)
print(c)