# 2. (Diameter, Circumference and Area of a Circle) Write a program that reads in the radius of
#  a circle as an integer and prints the circle’s diameter, circumference and area. Use the 
# constant value 3.14159 for π . Do all calculations in output statements.
r=int(input("Please enter radius of circle:"))
d=2*r
c=2*3.14159*r
a=3.14159*r**2
print("You enter radius of circle is:",r)
print("Thier diameter is:",d)
print("Thier circumference is:",c)
print("Thier area is:",a)
