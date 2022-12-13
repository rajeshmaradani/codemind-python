s=input()
s=s.upper()
s1=input()
s1=s1.upper()
for i in range(len(s)):
    if s[i] not in s1:
        print("False")
        break
    
else:
    print("True")
