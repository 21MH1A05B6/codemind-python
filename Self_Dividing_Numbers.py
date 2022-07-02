a = int(input())
b = int(input())
while a!=b+1:
    temp=a
    c=0
    f=0
    while temp%10!=0:
        d=temp%10
        temp//=10
        if a%d==0:
            c+=1
        f+=1
    if c==f and a%10!=0:
        print(a,end=" ")
    a+=1