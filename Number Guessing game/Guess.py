import random

guess = []
cpu_num = random.randint(1, 100)
player_num = int(input("Tell me which number i Guessed between 1 to 100: "))
guess.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print('!! You guessed to HIGH !!')
    else:
        print("!! You guessed to LOW !!")
    player_num = int(input("Enter Number: "))
    guess.append(player_num)
else:
    print("  CONGRATULATIONS  ")
    print("You have taken {} guesses".format(len(guess)))
    print(guess)
