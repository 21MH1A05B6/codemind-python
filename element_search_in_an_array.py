n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=1
for i in a:
    if i==x:
        c=0
if c==1:
    print(False)
else:
    print(True)