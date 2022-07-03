n=int(input())
temp=n
a=0
while temp:
    a+=1
    temp//=10
b=n
sum=0
while n:
    sum+=(n%10)**a
    n//=10
    a-=1
if sum==b:
    print(True)
else:
    print(False)