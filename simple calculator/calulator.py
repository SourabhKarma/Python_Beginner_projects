def add(a, b):
    return(a+b)


def substract(a, b):
    return(a-b)


def multiply(a, b):
    return(a*b)


def divide(a, b):
    return(a/b)


print("Select Operation: ")
print("1: Add ")
print("2: Substract ")
print("3: Multiply ")
print("4: Divide")

choice = int(input("Enter Choice 1/2/3/4: "))
num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

if choice == 1:
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 2:
    print(num_1, "-", num_2, "=", substract(num_1, num_2))
elif choice == 3:
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 4:
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("Invalid Input")
