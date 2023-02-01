import cv2
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    cv2.imshow("Virtual Mouse", frame)
    cv2.waitkey(1)