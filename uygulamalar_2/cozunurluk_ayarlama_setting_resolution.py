import cv2
import numpy as np

windowName = "Live Video"

cv2.namedWindow(windowName)  # pencere oluşturma

cap = cv2.VideoCapture(0)
print("Witdh : " + str(cap.get(3)))  # 3 en değerini verir
print("Height :" + str(cap.get(4)))  # 4 boy değerini verir

cap.set(3, 1280)
cap.set(4, 720)

print("Witdh* : " + str(cap.get(3)))  # 3 en değerini verir
print("Height* :" + str(cap.get(4)))  # 4 boy değerini verir

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
