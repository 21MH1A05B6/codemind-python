def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
temp=n
for i in range(n,2,-1):
    if prime(i):
        p=i
        break
while temp!=0:
    if prime(temp):
        q=temp
        break
    temp+=1
if (n-p)<(q-n):
    print(abs(n-p))
elif (n-p)==(q-n):
    print(abs(n-p))
else:
    print(abs(q-n))
            