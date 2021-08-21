import random

print("""Game Rules: \n
        "Rock vs Paper => Paper Wins" \n
        "Rock vs Scissor => Rock wins" \n
        "Paper vs Scissor => Scissor" \n """)

# Step 1: Conditions for the user

while True:
    print("Enter Choice 1: Rock, 2: Paper, 3: Scissor")
    user_choice = int(input("Your Turn: "))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter valid input: "))

    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissor"

    print("User's Choice is: " + user_choice_name)
    print("\nIt's Computer's Turn: ")

 # Step 2: Conditions for the computer

    comp_choice = random.randint(1, 3)

    while comp_choice == user_choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer's Choice is: " + comp_choice_name)
    print(user_choice_name + " v\s " + comp_choice_name)

 # Step 3: Condition of winning !!!

    if((user_choice == 1 and comp_choice == 2) or
            (user_choice == 2 and comp_choice == 1)):
        print("Paper Wins => ", end="")
        result = "Paper"

    elif((user_choice == 1 and comp_choice == 3) or
         (user_choice == 3 and comp_choice == 1)):
        print("Rock wins => ", end="")
        result = "Rock"
    else:
        print("Scissor Wins => ", end="")
        result = "Scissor"

 # Step 4: Printing the Winner

    if result == user_choice_name:
        print("** User Wins **")
    else:
        print("<** Computer Wins **>")

    print("Do you want to play again? (Y/N)")
    ans = input()

 # if user input n or N then break

    if ans == "n" or ans == "N":
        break


print("\n Thanks for playing")
