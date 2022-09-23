n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=s=0
c=[]
for i in range(n):
    if a[i]>=x and a[i]<=y:
        b+=1
        c.append(a[i])
if b==0:
    print("-1")
else:
    for i in c:
        s+=i
    print(s)