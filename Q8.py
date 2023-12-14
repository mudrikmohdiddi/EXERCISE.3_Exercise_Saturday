# 8. (Car-Pool Savings Calculator) Research several car-pooling websites. Create an application
# that calculates your daily driving cost, so that you can estimate how much money could be 
# saved by car pooling, which also has other advantages such as reducing carbon emissions 
# and reducing traffic congestion. The application should input the following information and 
# display the user’s cost per day of driving to work: 
# a) Total miles driven per day.
# b) Cost per gallon of gasoline.
# c) Parking fees per day.
# d) Average miles per gallon
# e) Tolls per day
save=0
tr=0
tc=0
p=0
e=0
t=0
tr=0
m=0
g=0
pa=0
av=0
to=0
n=0
while(n==0):
    print("_______________________________________________________")
    print("R---Enter Revenue")
    print("C---Enter Cost")
    print("S---Check your save")
    print("________________________________________________________")
    ch=input("Please enter your choice:")
    if(ch=="r" or ch=="R"):
        p=float(input("Enter car pooling revenue:"))
        e=float(input("Enter reducing carbon emissions revenue:"))
        t=float(input("Enter reducing traffic congestion revenue:"))
        tr=p+e+t
        print("Your total revenue is:",tr)
        save=save+tr
    elif(ch=="c" or ch=="C"):
        m=float(input("Enter Total miles driven par day:"))
        g=float(input("Enter Cost per gallon of gasoline:"))
        pa=float(input("Enter Parking fees per day:"))
        av=float(input("Enter Average miles per gallon:"))
        to=float(input("Enter Tolls per day:"))
        tc=m+g+pa+av+to
        print("Total cost is:",tc)
        save=save-tc
    elif(ch=="s" or ch=="S"):
        from datetime import datetime
        time=datetime.now()
        print(" ")
        print("_________________________________________________________________________________ ")
        print("Dear customer your remaining save up to now at ",time," is Tsh",save,"/-")
        print("_________________________________________________________________________________ ")
        print(" ")
    else:
        print("You enter wrong letter please try again")
        
        
        

    