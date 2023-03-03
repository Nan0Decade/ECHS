import random
import os


class image():

    def __init__(self, filename, extension, directory) -> None:
        # '''r - raw, s - size, p - pixels'''

        self.homedir = os.getcwd()
        os.chdir(directory)
        theImage = open(str(filename+extension), 'rb')

        self.name = filename
        self.extension = extension
        self.raw = list(theImage.read())
        self.glitchedRaw = self.raw

        theImage.close()
        os.chdir(self.homedir)

    def __str__(self) -> str:
        return str(self.raw)
    
    def saveImage(self) -> None:
        # create a dirctory
        # save the image to the directory

        try:
            os.chdir(str("glitched_photos"))
        except FileNotFoundError:
            os.mkdir(str("glitched_photos"))
            os.chdir(str("glitched_photos"))
        try:
            os.chdir(str(self.name + '_glitched'))
        except FileNotFoundError:
            os.mkdir(str(self.name + '_glitched'))
            os.chdir(str(self.name + '_glitched'))
        inDirectories = len(os.listdir())
        glitched = open(str(self.name + '_glitched_' + str(inDirectories+1) + self.extension), 'wb')
        glitched.write(bytes(self.glitchedRaw))
        glitched.close()
        os.chdir('..')
        os.chdir('..')

    def randomGlitchOne(self) -> None:
        glitchIndex = random.randint(0, len(self.glitchedRaw))
        self.glitchedRaw[glitchIndex] = random.randrange(0, 255)
    
    def randomGlitchTwo(self) -> None:
        randomIndex = random.randint(0, len(self.glitchedRaw))

        for i in range(-2, 2, 1):
            try:
                self.glitchedRaw[randomIndex+i] = random.randrange(0, 255)
            except IndexError:
                pass
            
    def glitch(self) -> None:
        

def main():
    directory = input('Enter the directory of the files you want to glitch: ')
    extension = input('Enter the extension of the file you want to glitch: ')
    numberOfPhotos = int(input('How many photos do you want to glitch? '))

    names = []

    for eachFile in os.listdir(directory):
        if eachFile.endswith(extension):
            # remove the extension
            eachFile = eachFile[:-len(extension)]
            names.append(eachFile)
            break
    
    for eachName in names:
        for i in range(numberOfPhotos):
            i = image(eachName, extension, directory)
            for t in range(random.randint(1, 200)):
                i.randomGlitch()
            i.saveImage()
    
    # print glitched photos
    print('Glitched photos:')
    for eachFile in os.listdir(directory):
        if eachFile.endswith(extension):
            print(eachFile)
    
main()
    


        
