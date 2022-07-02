n= int(input())
sum=0
while 1:
    if n==0 and sum>9:
        n=sum
        sum=0
    elif n==0 and sum<10:
        print(sum)
        break
    sum+=n%10
    n//=10