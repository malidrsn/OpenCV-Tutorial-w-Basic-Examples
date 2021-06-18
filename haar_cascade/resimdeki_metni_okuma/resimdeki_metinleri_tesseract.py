from PIL import Image
import pytesseract

img = Image.open("text.png")

text = pytesseract.image_to_string(image=img, lang="eng")

print(text)
