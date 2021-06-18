# image comparasion #eş olması için pixellerinde eşit olması gerekmektedir
import cv2
import numpy as np

img1 = cv2.imread("7.2 aircraft.jpg")
img1 = cv2.resize(img1, (640, 700))

img2 = cv2.imread("7.2 aircraft.jpg")
img2 = cv2.resize(img2, (640, 700))

img3 = cv2.medianBlur(img1, 7)  # deneme amacıyla yapıldı resim blurlandı ve onunla denendi

if img1.shape == img2.shape:
    print("Same Size")
else:
    print("Not same size")

# farkı arayalım difference

diff = cv2.subtract(img1, img2)  # subtract iki resmi karşılaştırıp farklı olan yerleri beyaz yapar
b, g, r = cv2.split(diff)  # resmi parçalayıp değerlerini döndürür

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:  # sıfır olmayanlari sayar

    print("Completely equal")
else:
    print("Completely Not equal")

cv2.imshow("AirCraft", img1)
cv2.imshow("AirCraft2", img2)
cv2.imshow("Diff", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
