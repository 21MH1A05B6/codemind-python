n=int(input())
w=0
r=2
for i in range(n):
    t=w
    w=r
    r+=t
print(w)