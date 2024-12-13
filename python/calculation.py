import cv2

def preprocess_image(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    rgb_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
    return rgb_image

def calculate_distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2) ** 0.5

def get_hand_center(hand_landmarks):
    x_list = [landmark.x for landmark in hand_landmarks.landmark]
    y_list = [landmark.y for landmark in hand_landmarks.landmark]
    center_x = sum(x_list) / len(x_list)
    center_y = sum(y_list) / len(y_list)
    return (center_x, center_y)

