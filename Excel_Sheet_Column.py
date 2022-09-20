n=int(input())
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2=''
while n>0:
    r=n%26
    if r==0:
        s2+="Z"
        n=(n//26)-1
    else:
        s2+=s1[r-1]
        n//=26
for i in range(len(s2)-1,-1,-1):
    print(s2[i],end='')