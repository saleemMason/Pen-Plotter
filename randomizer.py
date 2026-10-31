import random
import subprocess
from PIL import Image

sample_table_lowercase = { }
lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
copy_count = 2

for letter in lowercase_alphabet:
    token = []
    
    for number in range(1, copy_count + 1):
        token.append(letter + "_" + str(number))

    sample_table_lowercase[letter] = token

typed_letter = input("enter a letter: ").lower()

for letter in typed_letter:
    if letter in sample_table_lowercase:
        selected_token = random.choice(sample_table_lowercase[letter])
        
        print(selected_token)

        filename = selected_token + ".jpg"
        img = Image.open(filename)
        subprocess.run(["feh", filename])