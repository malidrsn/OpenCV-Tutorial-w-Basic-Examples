import cv2

cap = cv2.VideoCapture("6.2 car.mp4")

car_cascade = cv2.CascadeClassifier("2.1 car.xml")

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (480, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.2, 2)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("Frames", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
