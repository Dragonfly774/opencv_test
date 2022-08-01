import math

import cv2

face_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
# eye_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    # img = cv2.imread("nast.jpg")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_db.detectMultiScale(img_gray, 1.1, 19)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        img[y:y + h, x:x + w] = cv2.blur(img[y:y + h, x:x + w], (20, 20))
        face_rect = img_gray[y:y + h, x:x + w]
        eyes = eye_db.detectMultiScale(face_rect, 1.1, 19)
        for (ex, ey, ew, eh) in eyes:
            # img[y + ey:y + ey + eh, x + ex:x + ex + ew] = cv2.blur(img[y + ey:y + ey + eh, x + ex:x + ex + ew], (20, 20))
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 255), 1)

    cv2.imshow('res', img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
