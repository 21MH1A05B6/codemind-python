n=int (input())
sq=n*n
temp=n
rev=0
d=0
while temp:
    d+=1
    temp//=10
while d:
    rev=rev*10+sq%10
    sq//=10
    d-=1
rev1=0
while rev:
    rev1=rev1*10+rev%10
    rev//=10
if rev1==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')