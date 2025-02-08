import random


# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


# a function to generate a random int, or char
def generator():
    uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2 = chr(random.randint(65, 90))
    lowercaseLetter1 = chr(random.randint(97, 122))  # Generate a random lowercase letter (based on ASCII code)
    lowercaseLetter2 = chr(random.randint(97, 122))
    digit1 = chr(random.randint(48, 57))  # Generate a random digit (from 0 to 9) (based on ASCII code)
    digit2 = chr(random.randint(48, 57))
    punctuationSign1 = chr(random.randint(33, 47))  # Generate a random punctuation sign (based on ASCII code)
    punctuationSign2 = chr(random.randint(58, 64))

    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
    return shuffle(password)


# Ouput
print("Welcome to the password generator, that generates a 8 character password for you to use:")
print(f"Your new password is: {generator()}")
