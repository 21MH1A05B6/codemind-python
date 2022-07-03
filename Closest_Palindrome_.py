def is_palin(n):
    temp=n
    rev=0
    while temp!=0:
        r= temp%10
        rev=rev*10+r
        temp//=10
    if n==rev:
        return n

x = int(input())
for i in range(x-1,1,-1):
    if is_palin(i):
        a = i
        break
g = x+1
while g!=0:
    if is_palin(g):
        b = g
        break
    g+=1
if (x-a)<(b-x):
    print(a)
elif (x-a)==(b-x):
    print(a,b)
else:
    print(b)