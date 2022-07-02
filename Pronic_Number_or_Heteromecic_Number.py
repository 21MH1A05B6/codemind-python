n=int(input())
a=0
c=0
while a*(a+1)<=n:
    if a*(a+1)==n:
        print("YES")
        c=1
        break
    a+=1
if c==0:
    print("NO")