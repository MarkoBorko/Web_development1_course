a = input("Please enter first number: ")
b = input("Please enter second number: ")
arithmetic_operation = input("Please enter the arithmetic operation( +, -, *, / ): ")
if arithmetic_operation == "+":
    addition = int(a) + int(b)
    print("Addition of numbers " + a + ", " + b + " is: " + str(addition))
elif arithmetic_operation == "-":
    subtraction = int(a) - int(b)
    print("Subtraction of numbers " + a + ", " + b + " is: " + str(subtraction))
elif arithmetic_operation == "*":
    multiplication = int(a) * int(b)
    print("Multiplication of numbers " + a + ", " + b + " is: " + str(multiplication))
elif arithmetic_operation == "/":
    division = int(a) / int(b)
    print("Division of numbers " + a + ", " + b + " is: " + str (division))
else:
    print("Unknown operation.")
