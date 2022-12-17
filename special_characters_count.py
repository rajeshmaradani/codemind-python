s=input()
c=0
for i in s:
    j=ord(i)
    if j>32 and j<48 or j>57 and j<65 or j>90 and j<97 or j>121 and j<128:        c+=1
print(c)