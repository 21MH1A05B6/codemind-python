n=int(input())
z=0
o=0
t=0
th=0
f=0
fi=0
s=0
se=0
e=0
ni=0
while n:
    if n%10==0:
        z+=1
    elif n%10==1:
        o+=1
    elif n%10==2:
        t+=1
    elif n%10==3:
        th+=1
    elif n%10==4:
        f+=1
    elif n%10==5:
        fi+=1
    elif n%10==6:
        s+=1
    elif n%10==7:
        se+=1
    elif n%10==8:
        e+=1
    else:
        ni+=1
    n//=10

if z>1 or o>1 or t>1 or th>1 or f>1 or fi>1 or s>1 or se>1 or e>1 or ni>1:
    print("Not Unique Number")
else:
    print("Unique Number")
    
        