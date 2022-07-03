def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
d=0
while n<=m:
    if prime(n):
        d+=1
    n+=1
print(d)