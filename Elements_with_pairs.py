n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    print(a[i],end=' ')
if n%2:
    print("0")