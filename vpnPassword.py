import urllib.request
import pytesseract
from PIL import Image, ImageGrab
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'
def getBlock(wholeStringList, start, end):
    allBlocks = []
    s = ''
    tag = False
    for i in range(0, len(wholeStringList)):
        if start in wholeStringList[i] and not tag:
            tag = True
            s += wholeStringList[i]
        elif end in wholeStringList[i] and tag:
            tag = False
            s += wholeStringList[i]
            allBlocks.append(s)
            continue
        elif tag:
            s += wholeStringList[i]
    return s


if __name__ == '__main__':
    url = 'https://www.vpnbook.com/'
    codeSplit = urllib.request.urlopen(url)
    codeSplit = codeSplit.read().decode('utf-8').replace('\t', '').split('\r\n')
    codeSplit = getBlock(codeSplit, '<ul class="square">', '</ul>')
    img = codeSplit.split('<li><strong>Password: <img src=\"')[1].split('\" /></strong></li>')[0]
    urllib.request.urlretrieve('https://www.vpnbook.com/' + img, "code.jpg")
    print(pytesseract.image_to_string(Image.open('code.jpg')))