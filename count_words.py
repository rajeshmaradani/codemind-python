def count(s):
    m="aeiouAEIOU"
    if s[0] in m and s[len(s)-1] not in m:
        return True
    else:
        return False

s=input()
s1=s.split()
c=0
for i in s1:
    if count(i):
        c+=1
print(c)
