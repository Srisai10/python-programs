a=int(input("Enter a numbr:"))
b=int(input("Enter a number: "))
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        v=i
    i+=1
print("HCF of ",a, "and" ,b, ":",v)