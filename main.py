class Calculator:
    def add(self, x, y):
        """This function adds two numbers"""
        return x + y

    def subtract(self, x, y):
        """This function subtracts second number from the first one"""
        return x - y

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        return x * y

    def divide(self, x, y):
        """This function divides first number by the second one"""
        if y != 0:
            return x / y
        else:
            return "Error! Division by zero is not allowed."

# Initialize the calculator
calc = Calculator()

# Perform calculations
print(calc.add(5, 3))         # Output: 8
print(calc.subtract(5, 3))    # Output: 2
print(calc.multiply(5, 3))    # Output: 15
print(calc.divide(6, 3))      # Output: 2.0
print(calc.divide(10, 0))      # Output: Error! Division by zero is not allowed.
