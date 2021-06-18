# bir resmin diğer resim üzerinde olmasını inceliyoruz

import cv2
import numpy as np

img1 = cv2.imread("5.1 starwars.jpg")
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# img2_gray = cv2.imread("5.2 starwars2.jpg", 0)  # 1 yazarsak resmi 0 yazarsak gray format alırız
img2_gray = cv2.imread("5.2 starwars2.jpg", cv2.IMREAD_GRAYSCALE)  # bu da griye çevirir
# print(img2_gray.shape)   (117, 121) sonucunu verir 3 parametresi olsa renkli anlamınna gelirdi böyle gri formatta demek

w, h = img2_gray.shape[::-1]

result = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)

location = np.where(result >= 0.95)  # bu sayı yükseldikçe daha doğru oluyor

for i in zip(*location[::-1]):  # [:,:,-1] ile genişlik yüksekliği ters çiviriyoruz h,w oluyo
    cv2.rectangle(img1, i, (i[0] + w, i[1] + h), (0, 255, 0))

cv2.imshow("Image", img1)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
