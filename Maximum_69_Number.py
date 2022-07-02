n=int(input())
rev=0
sum=0
count=0
while n:
    rev=(rev*10)+n%10
    n//=10
while rev:
    if(rev%10==6 and count==0):
        sum=(sum*10)+9
        count+=1
    else:
        sum=(sum*10)+(rev%10)
    rev//=10
print(sum)
        