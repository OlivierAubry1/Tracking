import cv2

webcam = cv2.VideoCapture(0)
while True:
    success, feed = webcam.read()
    if success == False:
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("Counting finger",frame)
webcam.release()
cv2.destroyAllWindows()
