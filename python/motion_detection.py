import cv2
import mediapipe as mp
import numpy as np 
from picamera2 import Picamera2
import custom_module

import calculation
import function

def motion_detection():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands.Hands

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
    picam2.start() 

    with mp_hands(
        model_complexity=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
        max_num_hands=1) as hands:
        
        while True:
            image = picam2.capture_array()
            image = cv2.flip(image, 1)
            preprocessed_image = calculation.preprocess_image(image)
            preprocessed_image.flags.writeable = False
            results = hands.process(preprocessed_image)
            preprocessed_image.flags.writeable = True

            if results and results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    function.setting_flags(hand_landmarks)
                    function.hand_functions(function.gesture_flag, hand_landmarks)
                    
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp.solutions.hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(79, 79, 47), thickness=2, circle_radius=4),
                        mp_drawing.DrawingSpec(color=(34, 34, 178), thickness=2, circle_radius=2),
                    )

            cv2.imshow("Hand Detection", image)
            if cv2.waitKey(5) & 0xFF == 27:
                break

    picam2.stop()
    cv2.destroyAllWindows()
    
motion_detection()
