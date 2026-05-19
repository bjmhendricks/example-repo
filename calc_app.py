# Pseudocode
# Create a calulater app that store old calculations
# The app should ask the user for two number and which equation 
# equations.txt is where all the previous calulations will be stored and printed from


FILE = "equations.txt"

def calculate():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        op = input("Operation (+, -, *, /): ").strip()

# Calulations

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("Error: division by zero")  # Error detection
                return
            result = a / b
        else:
            print("Invalid operation")  # Error detection
            return

        equation = f"{a} {op} {b} = {result}"
        print("Result:", result)

        with open(FILE, "a") as f:
            f.write(equation + "\n")

    except ValueError:
        print("Please enter valid numbers.")

def show_equations():
    try:
        with open(FILE, "r") as f:
            print("Previous equations:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No saved equations yet.")  # If no equations are saved yet

def main():
    while True:
        print("1. Calculate")
        print("2. Show equations")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            calculate()
        elif choice == "2":
            show_equations()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
