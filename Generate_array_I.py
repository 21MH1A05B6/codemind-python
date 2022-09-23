n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    while a[i+1]:
        b.append(a[i])
        a[i+1]-=1
print(*b)