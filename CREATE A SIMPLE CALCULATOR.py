number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
selection = input("Enter the operation you want to perform (+, -, *, /, **, %, //): ")

# Print the first half of the equation
print(number1, selection, number2, "=", end=" ")

# Perform the actual calculation based on the selection
if selection == "+":
    print(number1 + number2)
elif selection == "-":
    print(number1 - number2)
elif selection == "*":
    print(number1 * number2)
elif selection == "/":
    # Optional: Check for division by zero
    if number2 == 0:
        print("Error (Division by Zero)")
    else:
        print(number1 / number2)
elif selection == "**":
    print(number1 ** number2)
elif selection == "%":
    print(number1 % number2)
elif selection == "//":
    if number2 == 0:
        print("Error (Division by Zero)")
    else:
        print(number1 // number2)
else:
    print("Invalid Operator")
