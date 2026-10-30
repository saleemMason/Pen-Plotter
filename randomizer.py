import random
import PIL

from PIL import image

sample_table_lowercase = { }
lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
copy_count = 2

for letter in lowercase_alphabet:
    token = []
    
    for number in range(1, copy_count + 1):
        token.append(letter + "_" + str(number))

        sample_table_lowercase[letter] = token

typed_letter = input("enter a letter: ")

for letter in typed_letter:
    if letter in sample_table_lowercase:
        print(random.choice(sample_table_lowercase[letter]))
        img = Image.open('a_2.jpg')