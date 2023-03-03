# open a image folder. Put everything in a list. select a random place.
# change the text to a random text (numbers and letters, special characters)
# save the text to a new text file with the same extensions as the image

import binascii
import os
import random
import string
import shutil

# set file as the image file\
# file = open('IMG_0083.jpg', 'r')

# asciiList = []

# convert file to hex

# fileSplit = list(file.read())

filename = 'IMG_0083.jpg'
with open(filename, 'rb') as f:
    content = f.read()


fileSplit = list(content)

randomIndex = random.randint(0, len(fileSplit))

randomText = random.choice(string.ascii_letters)

fileSplit[randomIndex] = randomText

glitched = open('IMG_0083_glitched.jpg', 'x')

glitched.write(fileSplit.join())

f.close()
glitched.close()
