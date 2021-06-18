# bir resmin histogramı o resmin aydınlık karanlık yollarını verir

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((500, 500), np.uint8) + 50
img = cv2.imread("klon.jpg")
# cv2.rectangle(img, (0, 60), (200, 150), (255, 255, 255), thickness=-1)
# cv2.rectangle(img, (200, 170), (350, 200), (255, 255, 255), thickness=-1)

b, g, r = cv2.split(img)  # bgr değerlerini ayırıyor
cv2.imshow("img", img)

plt.hist(b.ravel(), 256, [0, 256])  # b'nin histogramı
plt.hist(g.ravel(), 256, [0, 256])  # g'nin histogramı
plt.hist(r.ravel(), 256, [0, 256])  # r'nin hisrogramı

# plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
