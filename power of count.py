n=123
c=0
a=n
while n!=0:
    c+=1
    n//=10
while a!=0:
    d=a%10
    print(d**c)
    a//=10
