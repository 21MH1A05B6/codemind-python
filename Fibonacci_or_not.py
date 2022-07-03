n=int(input())
a=0
b=1
c=a+b
while c<n:
    c=a+b
    if(c<n):
        a=b
        b=c
if(c==n):
    print("True")
else:
    print("False")