import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255  # +255 dersek canvasın rengini beyaza çevirir

# print(canvas)


cv2.line(canvas, (50, 50), (512, 512), (255, 0, 0), thickness=5)
cv2.line(canvas, (100, 50), (200, 250), (0, 0, 255), thickness=1)

cv2.rectangle(canvas, (20, 20), (50, 50), (0, 255, 0),
              thickness=-1)  # içi dolu diktörtgen çizmek istiyorsak thickness değerini -1 yapıyoruz.

cv2.circle(canvas, (255, 255), 100, (0, 0, 255), thickness=5)  # içi dolu yapmak istersek thickness -1 yapıyoruz

# üçgen çizimi için özel bir yol yok fonksiyon yazmalıyız yada kendimize özel bir yöntem belirlemeliyiz.

p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

cv2.line(canvas, p1, p2, (0, 0, 0), 4)
cv2.line(canvas, p2, p3, (0, 0, 0), 4)
cv2.line(canvas, p1, p3, (0, 0, 0), 4)

points = np.array([[100, 200], [330, 200], [290, 220], [100, 100]], np.int32)
cv2.polylines(canvas, [points], True, (0, 0, 100),
              thickness=5)  # True olan değer birleştirme sağlıyor kapatıyor. false olsa kapamaz

cv2.ellipse(canvas, (300, 300), (80, 20), 0, 90, 360, (255, 255, 0), thickness=-1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
