n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1,2):
    if(a[i-1]<a[i] and a[i]>a[i-1]):
        c+=1
    else:
        print("-1")
        c=0
        break
if c!=0:
    print(c)