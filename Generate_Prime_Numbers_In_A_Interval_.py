def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True

n=int(input())
m=int(input())
for i in range(n+1,m+1):
    if prime(i):
        print(i)