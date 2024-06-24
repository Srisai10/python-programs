
#sum of the numbers which are divisible by 3
'''i=1
s=0
while i<=15:
    if i%3==0:
        s=s+i
        print(s)
    i+=1
print("Sum of the numbers is divisible by 3 :",s)'''


#Product  of the numbers which are divisible by 2,3,5
'''n=1
p=1
while n<=51:
    if (n%2==0) and (n%3==0) and (n%5==0):
        p=p*n  
    n+=1
print("Product of the numbr are divisibe by 2, 3,5 :",p)'''




#To print the divisor  of given number from 1 to 5
'''n=int(input("Enter the number: "))
i=1
s=0
while n<8:
    print("Divisors of :", n)
    while i<=n:
        if n%i == 0:
            s=s+i
           
            print(i)
            
        i+=1
    n+=1
print(s)'''


#to count odd numbers from 1 to 13.]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
'''i=1
c=0
while i<=13:
    if i%2!=0:
        c+=1
        print(i)
    i+=1
print("count odd number" , c)'''

#to find divisor to the give number
n=int(input("Enter a number: "))
i=1
while i<=n:
    if(n%i==0):
        print(i)
    i+=1

    