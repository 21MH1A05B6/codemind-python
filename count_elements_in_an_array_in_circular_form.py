n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(0,n-1):
    if i==0:
        if (a[i+1]%2 and a[n-1]%2==0)or(a[i+1]%2==0 and a[n-1]%2):
            count+=1
    if i!=0:
        if ((a[i-1]%2 and a[i+1]%2==0)or(a[i-1]%2==0 and a[i+1]%2)):
            count+=1
if (a[0]%2 and a[n-2]%2==0) or (a[0]%2==0 and a[n-2]%2):
    count+=1
print(count)