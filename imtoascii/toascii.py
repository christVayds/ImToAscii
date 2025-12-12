from PIL import Image

class ToAscii:

    def __init__(self, filename):
        self.filename = filename
        #self.asciiChars = "@%#*+=-:. "
        self.asciiChars = ["@%#*+=-:. ", "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\\\"^.\'` "]
        self.centeredDot = ' ······'

        self.good = True
        try:
            self.image = Image.open(filename)
        except FileNotFoundError:
            print("File Not Found")
            self.good = False

    def resize(self, newwidth=80):
        width, height = self.image.size
        ratio = height / width
        newheight = int(newwidth * ratio * 0.55)
        self.image = self.image.resize((newwidth, newheight))

    def grayscale(self):
        self.image = self.image.convert("L")

    def pixelToAscii(self, level=0):
        pixels = self.image.getdata()
        ascii_str = ''
        for pixel in pixels:
            ascii_str += self.asciiChars[level][::-1][pixel * (len(self.asciiChars[level]) - 1) // 255]
        return ascii_str

    def pixelToDotAscii(self):
        pixels = self.image.getdata()
        ascii_dots = ''
        for pixel in pixels:
            ascii_dots += self.centeredDot[pixel * (len(self.centeredDot) -1) // 255]

        return ascii_dots

    def show(self, ascii_str):
        ascii_width = self.image.width
        result = ""

        for i in range(0, len(ascii_str), ascii_width):
            result += ascii_str[i:i+ascii_width] + '\n'

        return result
