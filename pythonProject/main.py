import cv2

camera = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.2, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for x,y,w,h in eyes:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (150,255,150),3)

    cv2.imshow('Frunze', frame)

    if cv2.waitKey(1) == ord('q'):
        break
