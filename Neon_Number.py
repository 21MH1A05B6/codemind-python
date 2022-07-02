n=int(input())
pro=n*n
sum=0
while pro:
    sum+=pro%10
    pro//=10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")