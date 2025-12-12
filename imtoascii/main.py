"""
Let's Play Ascii
    1. Image to ascii
        main.py imtoascii <filename> <size ex. 80> <ascii level ex. 0>
    2. Camera to ascii
        main.py vidtoascii
    3. Video to ascii
        main.py vtoascii

"""


import sys
from toascii import ToAscii
from camera import Camera

def cam():
    camera = Camera(0)
    camera.checkCamera()
    try:
        camera.run()
    except KeyboardInterrupt:
        print("Program Quit")

def main():
    args = sys.argv
    if not len(args) > 1:
        cam()
        return

    # python3 main.py imtoascii home/christian/Downloads/anim1.png 80 1
    if args[1] == 'imtoascii':
        image = ToAscii(args[2])
        if image.good:
            image.resize(int(args[3]))
            image.grayscale()
            ascii_str = image.pixelToAscii(int(args[4]))
            #ascii_dot = image.pixelToDotAscii()
            result = image.show(ascii_str)
            print(result)
    elif args[1] == 'vidtoascii':
        cam()
    else:
        print(f"Undefined Command {args[1]}")

if __name__=='__main__':
    main()
