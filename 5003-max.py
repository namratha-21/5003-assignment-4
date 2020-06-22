a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
 
if (a > b) and (b > c):
   max = a
elif (b > a) and (b > c):
   max = b
else:
   max = c
 
print("The max of 3 numbers is",max)