# 5. (Digits of an Integer) Write a program that inputs a five-digit integer, separates the integer 
# into its digits and prints them separated by three spaces each. [Hint: Use the integer division 
# and modulus operators.] For example, if the user types in 42339, the program should print:
# 4 2 3 3 9
import math
k=0
while(k==0):
    print(" ")
    p=input("Please enter only five digit integer:")
    f=str(float(p))
    x,y,z=f.partition('.')
    z1=int(z)
    print(" ")
    if(z1==0):
        if(int(p)>=10000 and int(p)<=100000):
            n=int(p)
            a=n//10000
            b=(n%10000)//1000
            c=((n%10000)%1000)//100
            d=(((n%10000)%1000)%100)//10
            e=n%10
            s=str("   ")
            print("You enter five-digit integers:",n)
            print("Thier separation by three spaces is:",a,s,b,s,c,s,d,s,e)
        else:
            print("You enter integer which are not five integer.This is ivalid value, please try again")
    elif(z1>0):
        print("You enter float is invalid input, please try again")
    else:
        print("Not define")
        
        
        




