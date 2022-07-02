n=int(input())
a=0
b=1
temp=n
c=a+b
while c<=temp:
    c=a+b
    a=b
    b=c

if (n-a>b-n):
    print(b)
elif(n-a<b-n):
    print(a)
else:
    print(a,b)