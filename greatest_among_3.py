num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
greatest_number = 0
if(num1>num2)and(num1>num3):
    greatest_number = num1
elif(num2>num3)and(num2>num1):
    greatest_number = num2
else:
    greatest_number = num3
    print(greatest_number)