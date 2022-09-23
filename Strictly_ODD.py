n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]%2 and i%2==0:
        c+=1
if c==0:
    print(True)
else:
    print(False)