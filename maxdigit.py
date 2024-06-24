a=12945678
m=0
while a!=0:
    d=a%10
    if d>m:
        m=d
    a//=10
print("Maximum digit:",m)