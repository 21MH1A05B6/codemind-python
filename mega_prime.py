def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=d=0
if prime(n):
    while n:
        if prime(n%10):
            c+=1
        d+=1
        n//=10
    if c==d:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")