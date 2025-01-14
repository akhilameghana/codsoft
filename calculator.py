def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
def power(x, y):
    return x ** y
def square_root(x):
    if x < 0:
        return "Square root of negative number is not real!"
    return x ** 0.5
def main():
    print("Welcome to Simple Calculator!")
    while True:
        print("\nOperations available:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Quit")
        choice = input("Enter operation number (1-7): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number to find square root: "))
            print(f"Square root of {num} = {square_root(num)}")

        elif choice == '7':
            print("Thank you for using Simple Calculator!")
            break

        else:
            print("Invalid input. Please enter a valid number (1-7).")

if __name__ == "__main__":
    main()
