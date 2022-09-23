n = int(input())
a = list(map(int,input().split()))
if n%2:
    f = a[0:(n//2)+1]
    l = a[n-1:n//2:-1]
else:
    f = a[0:(n//2)]
    l = a[n-1:n//2-1:-1]
if n%2:
    l.append(0)
for i in range(len(f)):
    print(f[i],l[i],end=" ")