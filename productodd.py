n=int(input("enter:"))
i=1
p=1
while i<=n:
    if(i%2!=0):
        p*=i
    i+=1
print("product", p)
f=True
j=1
while f:
    if p%j==0:
        f=False
    j+=1
if f==True:
    print("perfect")
else:
    print("not ")
