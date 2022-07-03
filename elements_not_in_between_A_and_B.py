n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
x = 0
for i in a:
    if i not in range(b,c+1):
        print(i,end=' ')
        x = 1
if x==0:
    print("-1")