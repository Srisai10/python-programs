n=int(input("Enter a number:"))
i=1
s=0
while i<=n:
    if i%2!=0:
        s+=i
        print(i)
    i+=1
print(s)
f=True
j=2
while f:
    if s%j==0:
        f=False
    j+=1
if (f==True):
    print("Prime")
else:
    print("not Prime")