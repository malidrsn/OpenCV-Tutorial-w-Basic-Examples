# başarısız
import cv2
import numpy as np

img = cv2.imread("2.3 car.jpg")

# casede dosyamızı ekliyoruz
car_cascade = cv2.CascadeClassifier("2.1 car.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1, 2)
# faces 4 parametreye sahiptir
# x ve y başlangış noktaları w ve h en boy oranları

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
