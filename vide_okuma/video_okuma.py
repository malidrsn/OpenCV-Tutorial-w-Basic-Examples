import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) //webcam'den görüntü almak
cap = cv2.VideoCapture("MehmetAliDURSUN-202085151074.mp4")  # videodan görüntü almak

while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
