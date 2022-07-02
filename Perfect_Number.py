n = int(input())
sum=0
x=1
while x<=n//2:
    if n%x==0:
        sum+=x
    x+=1
if sum==n:
    print(True)
else:
    print(False)