from PIL import Image, ImageGrab
import time
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'


smallBox = (84, 84)
bigBox = (smallBox[0]*7, smallBox[1]*7)
boxToReadName = (82, 17)
boxToReadAmount = (24, 21)#(47, 21)
StartingPoint = (986, 440)

def grayScale(imageName):
    img = Image.open(imageName)
    gray = img.convert('L')
    #gray.save(imageName)
    bw = gray.point(lambda x: 0 if x < 90 else 255, '1')
    bw.save(imageName)

def readImage(imageName):
    grayScale(imageName)

    #pytesseract.image_to_string(Image.open(imageName), lang='eng')

    #img = cv2.imread(imageName)
    return pytesseract.image_to_string(Image.open(imageName))#, lang='eng')
    #return pytesseract.image_to_string(img)

def getAmmoBox():
    count = 0

    overallImage = ImageGrab.grab(bbox=(986, 440, 986 + bigBox[0], 440 + bigBox[1]))
    overallImage.save('OverallImage.png')

    for i in range(0, 7):
        for j in range(0, 7):
            Namex1 = StartingPoint[0] + (smallBox[0] * j) + (smallBox[0] - boxToReadName[0])
            Namey1 = StartingPoint[1] + (smallBox[1] * i)
            Namex2 = StartingPoint[0] + (smallBox[0] * (j + 1))
            Namey2 = Namey1 + boxToReadName[1]

            Ammountx1 = StartingPoint[0] + (smallBox[0] * j) + (smallBox[0] - boxToReadAmount[0])
            Ammounty1 = StartingPoint[1] + (smallBox[1] * i) + (smallBox[1] - boxToReadAmount[1])
            Ammountx2 = StartingPoint[0] + (smallBox[0] * (j + 1))
            Ammounty2 = StartingPoint[1] + (smallBox[1] * (i + 1))

            imageName = ImageGrab.grab(bbox=(Namex1, Namey1, Namex2, Namey2))
            imageAmmount = ImageGrab.grab(bbox=(Ammountx1, Ammounty1, Ammountx2, Ammounty2))

            imageName.save('images/Name/imageName' + str(count) + '.png')
            imageAmmount.save('images/Amount/imageAmount' + str(count) + '.png')

            textName = readImage('images/Name/imageName' + str(count) + '.png').replace('\n', '').replace(chr(12), '')
            textAmount = readImage('images/Amount/imageAmount' + str(count) + '.png').replace('\n', '').replace(chr(12), '')
            print('imageName' + str(count), ': ', textName, ', imageAmount' + str(count), ': ', textAmount)
            count += 1









if __name__ == '__main__':
    time.sleep(3)
    getAmmoBox()
