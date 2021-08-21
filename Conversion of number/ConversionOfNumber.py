''' while True:
    number = int(
        input("Enter a Number to Convert in Binary,Octal,Hexadecimal: "))
    if number == int(number):

        print("Binary value is: {}".format(bin(number)))
        print("Octal value is: {}".format(oct(number)))
        print("Hexadecimal value is: {}".format(hex(number)))
    else:

        print("Enter a ineger value")'''

#number = int(input("Enter a Number to Convertin Binary,Octal,Hexadecimal: "))


def conv():
    print("Binary value is: {}".format(bin(number)))
    print("Octal value is: {}".format(oct(number)))
    print("Hexadecimal value is: {}".format(hex(number)))


while True:
    try:
        number = int(
            input("Enter a Number to Convertin Binary,Octal,Hexadecimal: "))
        break
    except ValueError:
        print("Please input integer only...")
        continue

#print("num:", num)


conv()
