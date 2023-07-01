for i in range(int(input())):
    s=input()
    c=0
    for i in s:
        if ord(i)>=48 and ord(i)<57:
            c+=1
            break
    if c==0:
        print('No')
    else:
        print('Yes')