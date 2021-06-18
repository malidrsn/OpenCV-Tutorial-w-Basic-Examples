import cv2
import numpy as np
import pytesseract
import imutils

img = cv2.imread("licence_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# filtreleme işlemleri gürültü yok etme işlemleri

filtered = cv2.bilateralFilter(gray, 7, 250, 250)

# köşe bulma algoritması

edges = cv2.Canny(filtered, 30, 200)

# conturları arayacaz

contours = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print("Kontur ", contours)

cnts = imutils.grab_contours(contours)
# print(" Grab cnts : ", cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]  # 0 dan 10a kadar değerleri al
# print("Sıralanmış Cnts:", cnts)

screen = None

for c in cnts:
    epsilon = 0.018 * cv2.arcLength(c, True)  # deneyel yaklaşım uyguluyoruz. kareleri düzeltmek için
    approx = cv2.approxPolyDP(c, epsilon, True)  # konturları yakınlaştırıyor
    if len(approx) == 4:  # 4 köşe var ise anlamında
        screen = approx
        break

# maske uygulayacaz

mask = np.zeros(gray.shape, np.uint8)
# print(screen)
new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)

new_img = cv2.bitwise_and(img, img, mask=mask)

# kırpma
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))

crop = gray[topx:bottomx + 1, topy:bottomy + 1]
print(np.where(mask == 255))

# text okuma

text = pytesseract.image_to_string(crop, lang="eng")
print("Detected Plate is :", text)

# ekranda gösterme
cv2.imshow("Licence Plate Original", img)
cv2.imshow("Licence Plate Gray", gray)
cv2.imshow("Licence Plate Filtered", filtered)
cv2.imshow("Licence Plate Edged", edges)
cv2.imshow("Licence Plate Masked", mask)
cv2.imshow("Licence Plate New image", new_img)
cv2.imshow("Licence Plate New Cropped", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
