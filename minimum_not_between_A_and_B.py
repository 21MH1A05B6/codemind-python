n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
c=[]
d=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        b.append(a[i])
for i in range(n):
    if a[i] not in b:
        d+=1
        c.append(a[i])
if d==0:
    print("-1")
else:
    print(min(c))