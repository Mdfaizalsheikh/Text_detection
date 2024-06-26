from PIL import Image
import pytesseract
import numpy as np

filename = 'Cheque.png'
image_1= Image.open(filename)
image_1.show()
text = pytesseract.image_to_string(image_1)


print(text[:-1])
