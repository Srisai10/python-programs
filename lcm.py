'''n1=3
n2=6
lcm=True

if n1>n2:
    l=n1
else:
    l=n2
while lcm:
    if l%n1==0 and l%n2==0:
        lcm=False
        print(l)
    else:
        l+=1
        print(l)
print("lcm of" , n1 ,"and" , n2 ,":", l )'''


#LCM
n1=6
n2=12
c=0
i=1
while c<1:
    if i%n1==0 and i%n2==0:
        print(i)
        c+=1
    i+=1