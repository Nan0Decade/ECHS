from PIL import Image
import random


class Glitch_Image():

    def __init__(self, filename, extension, dataType):
        # '''r - raw, s - size, p - pixels'''
        theImage = Image.open(str(filename+extension))

        self.name = filename
        self.extension = extension
        self.raw = list(theImage.tobytes())
        self.size = theImage.size
        self.pixels = list(theImage.getdata())
        self.type = dataType

        self.newData = []

        if dataType == 'r':
            self.newData = self.raw
        elif dataType == 'p':
            self.newData = self.pixels

    def __str__(self) -> str:
        return str(self.raw)

    def saveImage(self):
        if self.type == 'r':
            glitched = Image.frombytes('RGB', self.size, bytes(self.newData))
        elif self.type == 'p':
            glitched = Image.new('RGB', self.size)
            glitched.putdata(self.newData)
        glitched.save(str(self.name + '_glitched' + self.extension))

    def pixelShuffle(self):
        random.shuffle(self.newData)

    def editSomeRawPlaces(self):  # does not work
        for i in range(300):
            index = random.randint(0, len(self.newData))
            self.newData[index] = (random.randrange(0, 255))
            count = 1
            for t in range(100):
                try:
                    self.newData[index + count] = (random.randrange(
                        0, 255))
                except IndexError:
                    pass
                try:
                    self.newData[index - count] = (random.randrange(
                        0, 255))
                except IndexError:
                    pass
                count += 15

    def replaceSomePixels(self):
        for i in range(300):
            index = random.randint(0, len(self.newData))
            self.newData[index] = (random.randrange(
                0, 255), random.randrange(0, 255), random.randrange(0, 255))
            count = 1
            for t in range(100):
                try:
                    self.newData[index + count] = (random.randrange(
                        0, 255), random.randrange(0, 255), random.randrange(0, 255))
                except IndexError:
                    pass
                try:
                    self.newData[index - count] = (random.randrange(
                        0, 255), random.randrange(0, 255), random.randrange(0, 255))
                except IndexError:
                    pass
                count += 1

filename = input('Enter the name of the file you want to glitch without extension: ')
extension = input('Enter the extension of the file you want to glitch: ')
dataType = str(input('Enter the type of data you want to glitch: '))

theImage = Glitch_Image(filename, extension, dataType)

theImage.editSomeRawPlaces()
theImage.saveImage()
