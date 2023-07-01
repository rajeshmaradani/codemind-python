for i in range(int(input())):
    n=input()
    l=len(n)
    if n==n[::-1] and l%2==0:
        print('YES EVEN')
    elif n==n[::-1] and l%2!=0:
        print('YES ODD')
    else:
        print('NO')