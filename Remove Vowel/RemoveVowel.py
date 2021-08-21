vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
message = input("Enter Message: ")

New_Message = ""

for letters in message:
    if letters not in vowels:
        New_Message = New_Message+letters

print("Message without vowels: {}".format(New_Message))
