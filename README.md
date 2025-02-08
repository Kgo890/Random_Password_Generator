For this challenge, we will use a Python script to generate a random password of 8 characters. Each time the program is run, a new password will be generated randomly. The passwords generated will be 8 characters long and will have to include the following characters in any order:

2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # etc.
To solve this challenge we will have to generate random characters and to do so we will need to use the ASCII code.

ASCII Code

The ASCII code (Pronounced ask-ee) is a code for representing English characters as numbers, with each character assigned a number from 0 to 127. For example, the ASCII code for uppercase M is 77. The extended ASCII code contains 256 characters (using numbers from 0 to 255).
To see a list of the most useful ASCII codes you can download our simplified ASCII helpsheet.

Using Python you can easily access ASCII values of a character using the ord() function. For instance ord(“M”) returns 77 and chr(77) returns “M”

When looking at the list of most widely used ASCII codes you will notice that all uppercase letters from A to Z have an ASCII code between 65 (=A) and 90 (=Z). To generate a random uppercase letter between A and Z we can hence use the following Python code:

import random
uppercaseLetter=chr(random.randint(65,90)) #Generate a random Uppercase letter (b
