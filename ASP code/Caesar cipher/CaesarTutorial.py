# THIS FILE WASN'T BUILT TO BE COMPILED
# IT WILL CRASH IF YOU TRY....

# Python Caesar cipher building tutorial

# The Caesar cipher works by shifting each letter of
# an input by a specified amount (key) on the alphabet

# If the key was 2 then:
#   a -> c
#   b -> d
#   x -> z

# And so on, we are going to write a script that does
# this for us.


# ----------------------------------------------------- #


# Step 1 - Encrypting a char

# We can take the ASCII value of a char, add on a key
# and we have an encrypted char:

letter = 'a'
key = 2
newValue = ord(letter) + key
newLetter = chr(newValue)

print(newLetter)

# ----------------------------------------------------- #

ord()
# returns the ASCII value of a char as an int
chr()
# returns the char of an ASCII value


# ----------------------------------------------------- #


# Step 2 - Encrypting a word

# We will use a loop to iterate over a word, Encrypting
# each char, since a string is an array of characters

message = "hello"
output = ""
key = 5

for x in range(len(message)):
    newValue = ord(message[x]) + key
    newLetter = chr(newValue)
    output = output + newLetter

print(output)

# ----------------------------------------------------- #

len(message)
# returns the length of a string, we need to
# know how many characters to loop through

output = output + newLetter
# adds the newly encrypted char
# onto the output variable within each iteration of the loop


# ----------------------------------------------------- #


# Step 3 - Encrypting a sentence

# We now have punctuation to deal with, but there's a few
# ways to deal with this. In this tutorial we will get rid of
# any characters not found in the alphabet.

sentence = "This, IS. A test!?!?"
message = sentence.lower()
output = ""
key = 10

for x in range(len(message)):
  if message[x] == ' ':
      output += ' '
      continue

  if ord(message[x]) < 97 or ord(message[x]) > 122:
      continue

  newValue = ord(message[x]) + key

  if newValue > 122:
      newValue -= 26

  newLetter = chr(newValue)
  output = output + newLetter

print(output)

# ----------------------------------------------------- #

# Ok so there's a few things to talk about here...

message = sentence.lower()
# will change the sentence
# to all lower case, this is needed since upper case letters
# have different ASCII values from lower case letters

continue
# skips to the next iteration in the loop

if message[x] == ' ':
    output += ' '
    continue
# This adds spaces to the output where found in the input

if ord(message[x]) < 97 or ord(message[x]) > 122:
    continue
# Skips the current iteration of the loop if the current
# letter isn't in the alphabet

if newValue > 122:
    newValue -= 26
# When the new value is higher than 122 (z), we take off 26, looping
# back round to the start of the alphabet again.


# ----------------------------------------------------- #


# Step 4 - Functions and Decryption

# Decryption works the same as encryption, we just need to take away
# the value of the key instead of adding it on

# Functions make it neater and nicer to look at

def Encryption(sentence, key):
    message = sentence.lower()
    output = ""

    for x in range(len(message)):
        if message[x] == ' ':
            output += ' '
            continue

        if ord(message[x]) < 97 or ord(message[x]) > 122:
            continue

        newValue = ord(message[x]) + key

        if newValue > 122:
            newValue -= 26

        newLetter = chr(newValue)
        output = output + newLetter

    return output


def Decryption(sentence, key):
    message = sentence.lower()
    output = ""

    for x in range(len(message)):
        if message[x] == ' ':
            output += ' '
            continue

        if ord(message[x]) < 97 or ord(message[x]) > 122:
            continue

        newValue = ord(message[x]) - key

        if newValue < 97:
            newValue += 26

        newLetter = chr(newValue)
        output = output + newLetter

    return output

# Now lets try interacting with the functions

encryptedMessage = Encryption("this is a test", 20)
print(encryptedMessage)

decryptedMessage = Decryption(encryptedMessage, 20)
print(decryptedMessage)
