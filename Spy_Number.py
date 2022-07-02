n=int(input())
sum=0
pro=1
while n:
    sum+=n%10
    pro*=n%10
    n//=10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")