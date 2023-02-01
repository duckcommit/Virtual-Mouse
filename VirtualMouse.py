import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, success = frame.shape
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
                if id==8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    pyautogui.moveTo(x, y)
                    

    if success:
        cv2.imshow("Virtual Mouse", frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows