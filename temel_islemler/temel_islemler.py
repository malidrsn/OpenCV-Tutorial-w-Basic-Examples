import cv2
import numpy as np

img = cv2.imread("klon.jpg")

dimension = img.shape
print(dimension)  # resim boyutunu öğrenme

color = img[300, 300]  # istenilen pixel'e ulaşma
print(color)

# bir pixele ait renklerin bulunması
blue = img[300, 300, 0]  # istenilen pixel'deki mavi rengin değeri
print("Blue : ", blue)

green = img[300, 300, 1]  # istenilen pixel'deki yeşil rengin değeri
print("Green : ", green)

red = img[300, 300, 2]  # istenilen pixel'deki kırmızı rengin değeri
print("Red : ", red)

# pixel'deki renklerin değiştirilmesi

img[300, 300, 0] = 250  # yeni blue değeri
print("Blue yeni değer : ", img[300, 300, 0])

# item ve itemset ile renklerin değiştirilmesi
blue1 = img.item(150, 200, 0)
print("Blue1 : ", blue1)
img.itemset((150, 200, 0), 172)
print("yeni Blue1 : ", img[150, 200, 0])

cv2.imshow("Klon Asker", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
