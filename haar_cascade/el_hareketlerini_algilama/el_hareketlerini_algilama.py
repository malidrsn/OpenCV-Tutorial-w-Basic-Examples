import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while 1:
    try:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        kernel = np.ones((3, 3), np.uint8)

        roi = frame[100:300, 100:300]
        cv2.rectangle(frame, (100, 100), (300, 300), (255, 0, 0), thickness=1)

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        lower_skin = np.array([100, 20, 82], np.uint8)
        upper_skin = np.array([200, 255, 255], np.uint8)

        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        mask = cv2.dilate(mask, kernel, iterations=4)  # siyah noktaları beyazlaştırıyor
        mask = cv2.GaussianBlur(mask, (5, 5), 100)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        # konturların daha iyi çizilmesi için aşağıdaki işlem yapılmaktadır
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        hull = cv2.convexHull(cnt)

        areaHull = cv2.contourArea(hull)
        areaCnt = cv2.contourArea(cnt)

        areaRatio = ((areaHull - areaCnt) / areaCnt) * 100
        # convex detects kusurları bulcaz

        hull = cv2.convexHull(approx, returnPoints=False)  # true dersek contours false dersek indisler döner
        defects = cv2.convexityDefects(approx, hull)

        l = 0  # kusur sayısı

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])

            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            d = (2 * area) / a

            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

            if angle <= 90 and d > 30:
                l += 1
                cv2.circle(roi, far, 3, (255, 0, 0), thickness=-1)

            cv2.line(roi, start, end, (255, 0, 0), thickness=2)
        l += 1

        font = cv2.FONT_HERSHEY_SIMPLEX

        if l == 1:
            if areaCnt < 2000:
                cv2.putText(frame, "Put your hands in the box", (0, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                if areaRatio < 12:
                    cv2.putText(frame, "0", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
                elif areaRatio < 17.5:
                    cv2.putText(frame, "Best Luck", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    cv2.putText(frame, "1", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        elif l == 2:
            cv2.putText(frame, "2", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        elif l == 3:
            if areaRatio < 27:
                cv2.putText(frame, "3", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, "Ok", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        elif l == 4:
            cv2.putText(frame, "4", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        elif l == 5:
            cv2.putText(frame, "5", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        elif l == 6:
            cv2.putText(frame, "Reposition", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        else:
            cv2.putText(frame, "Reposition", (0, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("mask ", mask)
        cv2.imshow("Frame", frame)

    except:
        pass
    k = cv2.waitKey(5) and 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()