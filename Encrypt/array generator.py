import random
import string
import pyperclip

alphabet = string.ascii_lowercase

# Shuffle the letters randomly
shuffled_alphabet = random.sample(alphabet, len(alphabet))

# Convert the list of shuffled letters back to a string
unique_string = (shuffled_alphabet)


print(unique_string)