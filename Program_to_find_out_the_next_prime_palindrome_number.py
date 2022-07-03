def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
g=n+1
while g!=0:
    if prime(g):
        b=g
        rev=0
        while b:
            rev=rev*10+b%10
            b//=10
        if rev==g:
            print(g)
            break
    g+=1
            