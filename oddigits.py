#Odd digits in a given number
'''a=125679
print(f"odd digits in given number d:")
while a!=0:
    d=a%10
    if d%2==1:
        print(d)
    a//=10'''


#Even digits in a given number

a=125679
s=0
print(f"even digits in given number d:")
while a!=0:
    d=a%10
    if d%2==0:
        print(d)
        s+=d
    a//=10
print("Sum of the digits of even number",s)
