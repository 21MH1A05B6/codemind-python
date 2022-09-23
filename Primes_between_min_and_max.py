def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
mini=a.index(min(a))
maxi=a.index(max(a))
if mini<maxi:
    for i in range(mini,maxi+1):
        if prime(a[i]):
            c+=1
    print(c)
else:
    for i in range(maxi,mini+1):
        if prime(a[i]):
            c+=1
    print(c)