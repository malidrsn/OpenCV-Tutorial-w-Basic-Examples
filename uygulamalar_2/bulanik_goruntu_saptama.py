# blurry image detection

import cv2

img = cv2.imread("4.2 starwars.jpg")

blurry_image = cv2.medianBlur(img, 7)

laplacian = cv2.Laplacian(blurry_image,
                          cv2.CV_64F).var()  # bize threshold üstünde bir değer verir blur arttıkça laplacian değeri düşer
# print(laplacian)

if laplacian < 500:
    print("Resime Blur uygulanmış")
else:
    print("Blur uygulanmamış")

cv2.imshow("Image", img)
cv2.imshow("Blurry Image", blurry_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
