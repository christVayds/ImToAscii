import cv2
import sys
import time

class Camera:

    def __init__(self, camera:int=0):
        self.camera = cv2.VideoCapture(camera)
        self.asciiChars = '@%#*+=-:. '

    def run(self):
        cam = True
        while cam:
            ret, frame = self.camera.read()
            if not ret:
                print("faild to grab frame")
                break

            # grayscale
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #resize
            frame = self.resize(frame)

            #cv2.imshow("camera", frame)
            ascii_img = self.pixelToAscii(frame)
            sys.stdout.write("\033[H")
            sys.stdout.write(ascii_img)
            sys.stdout.flush()
            #time.sleep(0.5)
            #print(ascii_img)

        self.camera.release()
        cv2.destroyAllWindows()

    def resize(self, frame, nwidth:int = 100):
        h, w = frame.shape

        aspect_ratio = h / w
        nheight = int(nwidth * aspect_ratio * 0.55)
        resized = cv2.resize(frame, (nwidth, nheight))
        return resized

    def pixelToAscii(self, frame):
        lframe = []
        for pixels in frame:
            line = "".join(self.asciiChars[::-1][int(pixel / 255 * (len(self.asciiChars)-1))] for pixel in pixels)
            lframe.append(line)
        return '\n'.join(lframe)

    def show(self, ascii_str):
        result = ''
        for i in range(0, len(self.ascii_str), self.size[0]):
            result += ascii_str[i:i+self.size[0]] + '\n'

        return result

    def checkCamera(self):
        if self.camera.isOpened():
            return True
