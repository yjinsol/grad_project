import PIL
import cv2
from PIL import Image
import pytesseract
img_path = 'test.png'
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = PIL.Image.fromarray(img2)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract"
txt = pytesseract.image_to_string(img2, lang='kor')
print(txt)