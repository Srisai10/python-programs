a=4128
ma=a%10
mi=a%10
while a!=0:
    d=a%10
    if d>ma:
        ma=d
        print(ma)
    elif d<mi:
        mi=d
        print(mi)
    a//=10
print(ma-mi)