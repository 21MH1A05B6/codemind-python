n=int(input())
a=list(map(int,input().split()))
c=0
if a[0]>a[1]:
    for i in range(n-1):
        if i%2==0 and a[i]>a[i+1]:
            c+=1
        elif i%2 and a[i]<a[i+1]:
            c+=1
    if c==n-1:
        print("yes")
    else:
        print("no")
else:
    for i in range(n-1):
        if i%2==0 and a[i]<a[i+1]:
            c+=1
        elif i%2 and a[i]>a[i+1]:
            c+=1
    if c==n-1:
        print("yes")
    else:
        print("no")