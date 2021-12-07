import random


def generate(password_len):
    password = ""
    for i in range(password_len):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z",
                   "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
                   "u", "v", "w", "x", "y", "z"]
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", ";", ":", ",", ".", "<", ">",
                   "'", "\"", "\\", "/", "?", "|"]
        choices = ["number", "letter", "symbol"]

        choice = random.choice(choices)

        if choice == "number":
            password += str(random.choice(numbers))
        elif choice == "letter":
            password += str(random.choice(letters))
        else:
            password += str(random.choice(symbols))
    return password

while True:
    length = int(input("Enter the length of the password you want: "))

    print(f"Your new password is: {generate(length)}")
