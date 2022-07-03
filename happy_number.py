n=int(input())
import math
res=0
while n:
    r=n%10
    res+=pow(r,2)
    n//=10
    if(n==0 and res<10):
        if(res==1 or res==7):
            print("True")
        else:
            print("False")
    elif(n==0 and res>=10):
        n=res
        r=0
        res=0