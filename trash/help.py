
def hi(options):
    options.split()
    output = []
    if 


def openImage():
    filename = input(
        'Enter the name of the file you want to glitch without extension: ')
    extension = input('Enter the extension of the file you want to glitch: ')
    theImage = Image.open(str(filename+extension))
    Imagebytes = list(theImage.tobytes())
    return Imagebytes, theImage.size


def newImage(Imagebytes, filename, extension, imageSize):
    glitched = Image.frombytes('RGB', imageSize, bytes(Imagebytes))
    glitched.save(str(filename + '_glitched' + extension))


def randomIndex(x): return [g == random.randint(
    0, len(theBytes)) for g in range(x)]


def byte(x): return [g == random.randint(0, 255) for g in range(x)]


theBytes, theSize = openImage()
numberOfGlitches = int(input('How many glitches do you want? '))


listOfBytes = byte(numberOfGlitches)

for i in randomIndex(numberOfGlitches):
    Imagebytes[i] = listOfBytes[i]


def getData(Options, filename, extension):
    Output = {}
       if 'r' in options:
            Output["r"] = list(pil.tobytes())
        if 's' in options:
            Output["s"] = pil.size()
        if 'p' in options:
            Output["p"] = list(pil.getdata())

def glitchImage(ImageData, filename, extension):
    glitched = pil.frombytes('RGB', ImageData["s"], bytes(ImageData["r"]))
    glitched.save(str(filename + '_glitched' + extension))

def pixelShuffle(ImageData):
    random.shuffle(ImageData["p"])
    ImageData["r"] = ImageData["p"].tobytes()
    return ImageData