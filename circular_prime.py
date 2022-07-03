def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    else:
        return True
n=int(input())
rev=0
temp=n
if(prime(n)):    
    while(n):
        rev=rev*10+n%10
        n//=10
    if (prime(rev)):
        print ("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")