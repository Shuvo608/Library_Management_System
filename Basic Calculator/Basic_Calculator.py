print("Basic_Calculator Using Python 1st Project")

print("1. Addition:")
print("2. Subtraction:")
print("3. Multiplication:")
print("4. Division:")

option = int(input("Please Select an option:"))

if option == 1:
        num1 = int(input("Enter your 1st number:"))
        num2 = int(input("Enter your 2nd number:"))
        add = num1 + num2
        print("Addition is: " + str(add))

elif option == 2:
        num1 = int(input("Enter your 1st number:"))
        num2 = int(input("Enter your 2nd number:"))
        sub = num1 - num2
        print("Subtraction is: " + str(sub))

elif option == 3:
        num1 = int(input("Enter your 1st number:"))
        num2 = int(input("Enter your 2nd number:"))
        mul = num1 * num2
        print("Multiplication is: " + str(mul))

elif option == 4:
        num1 = int(input("Enter your 1st number:"))
        num2 = int(input("Enter your 2nd number:"))
        div = num1 / num2
        print("Division is: " + str(div))

else: 
        print("Invalid Input")


        

