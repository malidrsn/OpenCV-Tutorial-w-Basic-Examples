# çizgi bulma algoritması saptama
import cv2
import numpy as np

img = cv2.imread("3.2 h_line.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# kenny kenar yöntemi köşeleri bulmaya yarar

edges = cv2.Canny(gray, 75, 150)

# cv2.HoughLines()  çok işlemci yiyor o yüzden tercih edilmiyor
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50,
                        maxLineGap=200)  # tercih edilen bu ve çizgileri tespit ediyor ve maxlineGap ise çizgi aralıklarını dolduruyor
# print(lines)

for i in lines:
    x1, y1, x2, y2 = i[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

cv2.imshow("img", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
