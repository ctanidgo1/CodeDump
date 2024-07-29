import random
import string

#INSTRUCTIONS - Type your message in ms = ''. Run. You will be given the encrypted version and the secret, send both.

# write message here using only a-z, no spaces (not case-sensitive)
ms = "iamthegreatestcoderofalltime"

# array for encryption
a = ('p', 'b', 'u', 'w', 'k', 'd', 'p', 'x', 'z', 'n', 'g', 'r', 'l', 'o', 'h', 'q', 'v', 'y', 'e', 'm', 'f', 'a', 'j', 's', 'c', 't', 'i')
b = ('p', 'q', 'l', 'm', 'b', 'i', 'g', 'c', 'w', 'u', 'f', 'k', 'y', 'p', 't', 's', 'v', 'x', 'j', 'n', 'z', 'e', 'd', 'h', 'o', 'a', 'r')
c = ('p', 'q', 'm', 'd', 'n', 'p', 'u', 'i', 'j', 'l', 'c', 'h', 'k', 'e', 'w', 't', 'r', 'a', 'o', 'x', 's', 'f', 'g', 'b', 'z', 'y', 'v')
d = ('p', 'l', 'h', 'i', 'j', 't', 'b', 'y', 'm', 'c', 'f', 'n', 'a', 'e', 'r', 'p', 'd', 'w', 'v', 'o', 's', 'u', 'g', 'q', 'z', 'k', 'x')
e = ('p', 'p', 'c', 'b', 'z', 'q', 'm', 'g', 'u', 'w', 'n', 'v', 's', 'j', 'e', 'a', 'f', 'd', 'h', 'i', 'x', 'y', 'k', 'o', 'l', 't', 'r')
f = ('p', 'k', 's', 'e', 't', 'c', 'f', 'b', 'u', 'g', 'l', 'q', 'x', 'p', 'i', 'd', 'y', 'j', 'w', 'a', 'h', 'n', 'z', 'm', 'r', 'v', 'o')
g = ('p', 'x', 'p', 'l', 'j', 's', 'i', 'q', 'e', 'm', 'f', 'y', 'u', 'r', 'k', 'g', 'd', 'o', 'a', 'v', 't', 'z', 'w', 'n', 'b', 'c', 'h')
h = ('p', 'b', 'n', 'w', 'u', 'f', 's', 'r', 'o', 'q', 'a', 'c', 'd', 'i', 'z', 'j', 'g', 'v', 'h', 'k', 'x', 'e', 'm', 'l', 'p', 'y', 't')
i = ('p', 'x', 'q', 'i', 'e', 'p', 'c', 'h', 'm', 'a', 'n', 'r', 'v', 'b', 'g', 't', 'd', 'k', 'y', 'o', 'u', 'z', 'f', 'w', 's', 'j', 'l')
j = ('p', 'd', 'f', 'r', 'k', 'u', 'i', 'b', 'y', 'o', 'z', 'a', 'h', 's', 'n', 'q', 'l', 'm', 't', 'e', 'c', 'x', 'j', 'g', 'p', 'v', 'w')
k = ('p', 'y', 'k', 'u', 'b', 'z', 'c', 'p', 's', 'l', 'x', 'f', 'v', 'r', 'm', 'a', 't', 'w', 'n', 'o', 'i', 'j', 'h', 'e', 'q', 'd', 'g')
l = ('p', 'm', 'r', 'p', 'f', 'n', 'j', 'z', 'e', 'v', 'w', 't', 'u', 'l', 'x', 'y', 'c', 'g', 'h', 'd', 'a', 'i', 'k', 'b', 'q', 'o', 's')
m = ('p', 'h', 'e', 'v', 'a', 'b', 'l', 'c', 'm', 't', 'k', 'r', 'g', 'z', 's', 'u', 'y', 'j', 'f', 'n', 'd', 'q', 'w', 'x', 'i', 'o', 'p')
n = ('p', 'c', 'u', 'j', 'f', 'z', 'e', 'w', 'i', 'h', 'a', 'v', 's', 'x', 'o', 'l', 'm', 'k', 'b', 'n', 'p', 't', 'g', 'r', 'y', 'd', 'q')
o = ('p', 'v', 'q', 'b', 'o', 'n', 't', 'w', 'h', 'p', 'r', 'l', 'a', 'e', 'z', 'd', 'x', 'k', 'y', 'u', 'j', 'i', 'm', 'c', 'g', 'f', 's')
p = ('p', 'f', 'j', 'x', 'z', 'h', 'a', 'w', 'p', 'e', 't', 'r', 'v', 'l', 'n', 's', 'b', 'i', 'u', 'k', 'g', 'q', 'y', 'm', 'd', 'o', 'c')
q = ('p', 'v', 'k', 'u', 'o', 'h', 'd', 'w', 'm', 'f', 't', 'e', 'z', 'j', 'y', 'c', 'q', 'p', 'i', 'n', 's', 'r', 'b', 'x', 'g', 'l', 'a')
r = ('p', 'y', 'u', 'h', 'v', 'd', 'n', 'p', 'q', 'k', 'c', 'r', 'o', 'b', 'm', 'g', 'l', 't', 'j', 'f', 'x', 'e', 's', 'a', 'z', 'w', 'i')
s = ('p', 'w', 'n', 'r', 'a', 'd', 'y', 'u', 'c', 'x', 'g', 'f', 'p', 'h', 'o', 'v', 'z', 'q', 'i', 'k', 'l', 'e', 'm', 't', 's', 'b', 'j')
t = ('p', 'u', 'h', 'e', 't', 'f', 'g', 'v', 'y', 'c', 'k', 'b', 'j', 's', 'r', 'o', 'a', 'd', 'w', 'i', 'p', 'm', 'q', 'n', 'z', 'l', 'x')
u = ('p', 'e', 'u', 'j', 'y', 'g', 'r', 'p', 'c', 'd', 'o', 'v', 't', 'z', 'i', 'm', 'b', 'a', 'n', 'q', 'w', 'x', 'f', 'h', 'k', 's', 'l')
v = ('p', 'n', 'h', 'r', 'k', 'p', 's', 'l', 'u', 'j', 'f', 'w', 'v', 'd', 'a', 'y', 'g', 'e', 'o', 'x', 't', 'c', 'z', 'q', 'm', 'b', 'i')
w = ('p', 't', 'b', 'w', 'f', 'l', 'e', 'p', 'c', 'k', 'i', 'o', 'a', 's', 'd', 'n', 'x', 'm', 'y', 'u', 'r', 'z', 'q', 'j', 'v', 'h', 'g')
x = ('p', 'g', 'j', 'y', 'n', 'z', 'x', 'l', 's', 'u', 'h', 'm', 'p', 't', 'q', 'f', 'k', 'o', 'c', 'd', 'a', 'r', 'e', 'v', 'b', 'i', 'w')
y = ('p', 'f', 'p', 't', 'y', 'm', 'n', 'h', 'e', 'l', 'a', 'z', 'o', 'x', 'k', 'g', 'd', 'r', 'b', 'i', 'v', 'w', 'j', 'u', 'q', 's', 'c')
z = ('p', 'd', 'w', 'u', 'm', 'j', 'c', 'f', 'x', 't', 'h', 'e', 's', 'a', 'l', 'i', 'n', 'z', 'q', 'r', 'v', 'p', 'g', 'k', 'b', 'o', 'y')
# end array

# dont write message here
encrypt = ''

def exclude_characters(input_string, characters_to_exclude):
    return ''.join(char for char in input_string if char not in characters_to_exclude)
def letter_position(letter): # Convert to lowercase to handle both uppercase and lowercase letters
    if letter.isalpha():
        return ord(letter) - ord('a') + 1  # Subtract the ASCII value of 'a' to get the position
    else:
        return "Not a valid letter"

input_string = string.ascii_lowercase
characters_to_exclude = "xzsu"  # excluding vowels
result = exclude_characters(input_string, characters_to_exclude)

msg = ms.lower()
message = []

for letter in msg:
    message.append(letter)

length = len(message)

sec = ([random.choice(result) for _ in range(length)])
secret = [eval(s) for s in sec]

ind = 0
#print('Debugging (ignore)', sec)


while ind < length:
    id = letter_position(message[ind])
    #(print(secret[ind][id]))
    #print('Debugging, ignore', len(secret[ind]))
    encrypt = encrypt + (secret[ind][id])
    ind += 1
#print('Original plaintext:', ms)
print('Encrypted message:', encrypt)
print('Secret:', sec)









