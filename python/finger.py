import cv2
import mediapipe as mp

index_tip = None
index_pip = None

thumb_tip = None
thumb_ip = None

middle_tip = None
middle_pip = None
middle_dip = None

ring_tip = None
ring_pip = None
ring_dip = None

pinky_tip = None
pinky_pip = None
pinky_dip = None

def load_fingers(hand_landmarks):
    global index_tip, index_pip, thumb_tip, thumb_ip, middle_tip, middle_pip, middle_dip, ring_tip, ring_pip, ring_dip, pinky_tip, pinky_pip, pinky_dip
    
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    index_pip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_PIP]
    
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_IP]
   
    middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_pip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP]
    middle_dip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_DIP]
    
    ring_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    ring_pip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_PIP] 
    ring_dip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_DIP]
    
    pinky_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]
    pinky_pip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_PIP]
    pinky_dip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_DIP]
