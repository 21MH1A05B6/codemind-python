n=int(input())
a=list(map(int,input().split()))
#print(a)
for i in range(n-1,-1,-1):
    if a[i]%2:
        print(i)
        break