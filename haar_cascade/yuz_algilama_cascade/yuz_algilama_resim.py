import cv2
import numpy as np

img = cv2.imread("4.2 face.png")

# casede dosyamızı ekliyoruz
face_cascade = cv2.CascadeClassifier("4.3 frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3,
                                      7)  # 1.3 ölçeklemek için ve 4 değeri 4 pencere ile kıyaslayıp yüz olduğunu anlamak için
# faces 4 parametreye sahiptir
# x ve y başlangış noktaları w ve h en boy oranları

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
