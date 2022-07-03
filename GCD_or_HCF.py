n,m=map(int,input().split())
while (n!=m):
    if(n>m):
        n=n-m
    else:
        m=m-n
print(n)