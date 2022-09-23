n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
k=s/n
print("%.2f"%k)