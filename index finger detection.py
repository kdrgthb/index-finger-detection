import cv2
import mediapipe as mp
import pygame
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hand_model = mp.solutions.hands
hand_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
with  hand_model.Hands(min_tracking_confidence=0.5, min_detection_confidence=0.5) as hand:

    open= True
    while open :

        control, frame = cap.read()
        height,width,numbers = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(rgb)
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:

                for coor in hand_model.HandLandmark:
                    mark = hand_landmark.landmark[8]
                    x = int(mark.x*width)
                    y =int(mark.y*height)
                    cv2.circle(frame, (x, y), 5,(255,200,145),-1)


        cv2.imshow("forefinger detection", frame)
        if cv2.waitKey(15) == 27:
            break