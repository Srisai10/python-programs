n=int(input("Enter:"))
s=0
while n!=0:
    d=n%10
    s+=d
    n//=10
if s%2==0:
    print("even")
elif s%2!=0:
    print("odd")
