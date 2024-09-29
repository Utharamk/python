class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def menu(self):
        while True:
            print("\nCalculator Menu")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            choice = input("Enter your choice:")
            a = int(input("Enter the first number:"))
            b = int(input("Enter the second number:"))
                

            if choice == '1':
                print(f"Result: {self.add(a, b)}")

            elif choice == '2':
                print(f"Result: {self.subtract(a, b)}")

            elif choice == '3':
                print(f"Result: {self.multiply(a, b)}")

            elif choice == '4':
                print(f"Result: {self.divide(a, b)}")

            elif choice == '5':
                print("Exit")
                break

            else:
                print("Invalid")
calc = Calculator()
calc.menu()