# ------------------------------------> This is a simple calculator program that performs basic arithmetic operations. <-----------------------------
print("Welcome to the simple calculator!")
while True: 
    print("please select an operation : ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input(" Enter the number corresponding to the operatoin you want to perform : ")
    num1= float(input("Enter the first number : "))
    num2= float(input("Enter the second number : "))
    if operation == '1':
        result = num1 + num2
        print(f'The result of {num1} + {num2} is : {result}')
    elif operation == '2':
        result = num1 - num2
        print(f'The result of {num1} - {num2} is : {result}')
    elif operation == '3':
        result = num1 * num2
        print(f'The result of {num1} * {num2} is : {result}')
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f'The result of {num1} / {num2} is : {result}')
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected. Please choose a valid option.")
    continue_calculation = input("Do you want to perform another calculation? (yes/no) : ")
    if continue_calculation.lower() != 'yes':
        print("Thank you for using the simple calculator. Goodbye!")
        break
    
