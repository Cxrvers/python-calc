class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Please try again cannot divide by zero"
    

my_calculator = Calculator()

while True:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice  = int(input("Select operation: "))

    if choice == 5:
        break
    elif choice in (1, 2, 3, 4):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 4 & b == 0:
            b = int(input("Please enter another number cannot divide by 0: "))

        if choice == 1:
            print(a, '+', b, "=", my_calculator.add(a,b))
        elif choice == 2:
            print(a, "-", b, "=", my_calculator.subtract(a,b))
        elif choice == 3:
            print(a, "*", b, "=", my_calculator.multiply(a,b))
        elif choice == 4:
            print(a, "/", b, "=", my_calculator.divide(a,b))

    else:
        print("Invalid Input")
