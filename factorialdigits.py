'''n=123
a=n
while a!=0:
    d=a%10
    f=1
    while d!=0:
        f*=d
        d-=1
    print(f)
    a//=10'''

n=123
a=n
s=0
while a!=0:
    d=a%10
    f=1
    while d!=0:
        f*=d
        d-=1
    s+=f
    a//=10
print(s)
