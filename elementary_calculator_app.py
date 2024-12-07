while True : #The reason we use while True is to start an infinite loop in python.
    print("1. Operation:Summation")
    print("2. Operation:Differnce")
    print("3. Operation:Multiplication")
    print("4. Operation:Division")
    print("5. Operation:Nothing Operation")

    character= int(input())
    if character >= 1 and character <= 4:
        print("Please enter two numbers: ", end = "") # In this line, the `end=""` expression indicates that the `print()` function should not append a newline character at the end.
        num1 = float(input("Please enter first number:"))
        num2 = float(input("Please enter second number:"))
    if character == 1:
        result = num1 + num2
        print("Result:",result)
    elif character == 2:
        result = num1 - num2
        print("Result:",result)
    elif character == 3:
        result = num1 * num2
        print("Result:",result)
    elif character == 4:
        result = num1 / num2
        print("Result:",result)
    elif character == 5:
        print("You pressed the 5th operation for this reason nothing operation")
    else:
        print("Please enter valid number :()")