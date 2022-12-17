s=input()
c=0
for i in s:
    j=ord(i)
    if j>96 and j<123:
        c+=1
print(c)