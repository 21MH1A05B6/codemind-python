def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
for i in range(1,10):
    if prime(i+(n+m)):
        print(i)
        break