def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=0
for i in range(n):
    for j in range(n):
        if i*j==n:
            if prime(i) and prime(j):
                print(i,end=' ')
                c=1
if c==0:
    print("-1")