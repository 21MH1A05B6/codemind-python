n=int(input())
a=list(map(int,input().split()))
m=int(input())
s=0
for i in a:
    if i<=m:
        s+=i
print(s)