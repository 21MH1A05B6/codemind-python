n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if a[i]%2==0:
        b.append(a[i])
if len(b)==len(a):
    print(True)
else:
    print(False)