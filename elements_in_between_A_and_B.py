n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
b=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        c.append(a[i])
        b+=1
if b==0:
    print("-1")

else:
    print(*c)