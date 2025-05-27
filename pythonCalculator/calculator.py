# Fonksiyonlar
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

# Main kısım
while True:
    print("\nSelect an operation")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("You are exiting the calculator...")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid Selection! Please choose a number between 1 and 5.")

    # Notes (TR):
    # "def" fonksiyon tanımlar,
    # "try/except" hata yönetimi, hatalı girildiğinde çökmeyi engeller,
    # "break" döngüyü durdurur,
    # "continue" döngüyü atlar.

    # Project date: 19.05 - May 27 - 2025
