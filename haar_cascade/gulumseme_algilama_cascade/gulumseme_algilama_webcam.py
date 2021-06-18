import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("4.3 frontalface.xml")
smile_cascade = cv2.CascadeClassifier("4.2 smile.xml")

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.5, 6)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    roi_frame = frame[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]

    smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 9)

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_frame, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
