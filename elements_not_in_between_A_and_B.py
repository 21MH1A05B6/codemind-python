n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=[]
b=0
for i in range(0,n):
    if a[i]<x or a[i]>y:
        s.append(a[i])
        b+=1
if b==0:
    print("-1")
else:
    print(*s)