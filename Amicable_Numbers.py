a=int(input())
b=int(input())
i=1
sum=0
while i<=a//2:
    if a%i==0:
        sum+=i
    i+=1
i=1
if sum==b:
    sum=0
    while i<=b//2:
        if b%i==0:
            sum+=i
        i+=1
if sum==a:
    print("Amicable")
else:
    print("Not Amicable")