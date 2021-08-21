
def Encrypted():

    en_dict = {"A": "E", "B": "F", "C": "G", "D": "H", "E": "I", "F": "J", "G": "K", "H": "L", "I": "M", "J": "N", "K": "O", "L": "P", "M": "Q",
               "N": "R", "O": "S", "P": "T", "Q": "U", "R": "V", "S": "W", "T": "X", "U": "Y", "V": "Z", "W": "A", "X": "B", "Y": "C", "Z": "D", "1": "4", "2": "5",
               "3": "6", "4": "7", "5": "8", "6": "9", "7": "0", "8": "1", "9": "2", "0": "3", " ": " "}

    en_Message = input("Enter Message: ").upper()
    encrypted = ""

    for letter in en_Message:
        if letter in en_dict:
            encrypted += en_dict[letter]
        else:
            encrypted += letter

    print(encrypted.lower())


def Decrypted():

    de_dict = {"E": "A", "F": "B", "G": "C", "H": "D", "I": "E", "J": "F", "K": "G", "L": "H", "M": "I", "N": "J", "O": "K", "P": "L", "Q": "M",
               "R": "N", "S": "O", "T": "P", "U": "Q", "V": "R", "W": "S", "X": "T", "Y": "U", "Z": "V", "A": "W", "B": "X", "C": "Y", "D": "Z", "4": "1", "5": "2",
               "6": "3", "7": "4", "8": "5", "9": "6", "0": "7", "1": "8", "2": "9", "3": "0", " ": " "}

    de_Message = input("Enter Message: ").upper()
    decrypted = ""

    for letters in de_Message:
        if letters in de_dict:
            decrypted += de_dict[letters]
        else:
            decrypted += letters
    print(decrypted.lower())


Decrypted()
