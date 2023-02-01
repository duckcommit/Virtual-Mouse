import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
while True:
    success, frame = cap.read()
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    print(hands)
    if success:
        cv2.imshow("Virtual Mouse", frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows