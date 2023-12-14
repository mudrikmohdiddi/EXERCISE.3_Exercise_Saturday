# 1. Write a program that inputs three integers from the key-board and prints the sum, average, 
# product, smallest and largest of these numbers.
import statistics
a=int(input("Please enter first integer number:"))
b=int(input("Please enter second integer number:"))
c=int(input("Please enter third integer number:"))
s=a+b+c
mean=(statistics.mean([a,b,c]))
p=a*b*c
sm=min(a,b,c)
lg=max(a,b,c)
print("You enter first integer number is:",a)
print("You enter second integer number is:",b)
print("You enter third integer number is:",c)
print("Thier sum is:",s)
print("Thier average is:",mean)
print("Thier product is:",p)
print("Thier smallest is:",sm)
print("Thier largest is:",lg)