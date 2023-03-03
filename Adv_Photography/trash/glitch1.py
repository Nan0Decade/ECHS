import random
from PIL import Image

filename = input('Enter the name of the file you want to glitch without extension: ')
extension = input('Enter the extension of the file you want to glitch: ')
# width = int(input('Enter the width of the image you want to glitch: '))
# height = int(input('Enter the height of the image you want to glitch: '))
dimensions = (width, height)
with open(str(filename+extension), 'rb') as f:
    content = f.read()

fileSplit = list(content)

numberOfGlitches = int(input('How many glitches do you want? '))
randomIndex = lambda x: [g == random.randint(0, len(fileSplit)) for g in range(x)]

byte =  lambda x: [g == random.randint(0, 255) for g in range(x)]

listOfBytes = byte(numberOfGlitches)

for i in randomIndex(numberOfGlitches):
    fileSplit[i] = listOfBytes[i]

# image = Image.frombytes('RGB', dimensions, bytes(fileSplit))

# image.save(str(filename + '_glitched' + extension))

glitched = open(str(filename + '_glitched' + extension), 'x')
glitched.write(''.join(fileSplit).encode('base64'))
f.close()
glitched.close()

