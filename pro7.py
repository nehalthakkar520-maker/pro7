from datetime import datetime
import math
import random
import uuid

# Date and Time
def current_datetime():
    now = datetime.now()
    print("\nCurrent Date & Time :", now)

# Math Module
def math_operation():
    num = float(input("Enter Number : "))

    print("Square Root :", math.sqrt(num))

    if num >= 0:
        print("Factorial :", math.factorial(int(num)))

# Random Module
def random_number():
    print("Random Number :", random.randint(1, 100))

def generate_otp():
    print("OTP :", random.randint(1000, 9999))

# UUID Module
def generate_uuid():
    print("UUID :", uuid.uuid4())

# File Module
def write_file():
    text = input("Enter Text : ")

    file = open("data.txt", "a")
    file.write(text + "\n")
    file.close()

    print("Data Saved Successfully")

def read_file():
    try:
        file = open("data.txt", "r")
        print("\nFile Content:")
        print(file.read())
        file.close()

    except:
        print("File Not Found")

# Module Exploration
def module_info():
    print("\nMath Module Functions:")
    print(dir(math))

# Main Program
if __name__ == "__main__":

    while True:

        print("\n========== MULTI UTILITY TOOLKIT ==========")
        print("1. Current Date & Time")
        print("2. Math Operation")
        print("3. Random Number")
        print("4. Generate OTP")
        print("5. Generate UUID")
        print("6. Write File")
        print("7. Read File")
        print("8. Module Information")
        print("9. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            current_datetime()

        elif choice == "2":
            math_operation()

        elif choice == "3":
            random_number()

        elif choice == "4":
            generate_otp()

        elif choice == "5":
            generate_uuid()

        elif choice == "6":
            write_file()

        elif choice == "7":
            read_file()

        elif choice == "8":
            module_info()

        elif choice == "9":
            print("Thank You")
            break

        else:
            print("Invalid Choice")