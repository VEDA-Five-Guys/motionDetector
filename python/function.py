import calculation
import time
import custom_module
import finger

previous_hand_position = None
previous_time = None
presenting_flag = False
gesture_flag = 0

def setting_flags(hand_landmarks):
    global gesture_flag
    if is_pointing(hand_landmarks):
        gesture_flag = 1
    elif is_drawing(hand_landmarks):
        gesture_flag = 2
    elif is_stop(hand_landmarks):
        gesture_flag = 0

def hand_functions(gesture_flag, hand_landmarks):
    match gesture_flag:
        case 1:
                x_coord, y_coord = get_coordinates(hand_landmarks)
                custom_module.send_message(f"Pointing({x_coord}, {y_coord})")
        case 2:
                x_coord, y_coord = get_coordinates(hand_landmarks)
                custom_module.send_message(f"Drawing({x_coord}, {y_coord})")
        case 0:
            default_gesture(hand_landmarks)

def get_coordinates(hand_landmarks):
    finger.load_fingers(hand_landmarks)
    x_coord = int(finger.index_tip.x * 640)  # Frame width: 640
    y_coord = int(finger.index_tip.y * 480)  # Frame height: 480
    return x_coord, y_coord 

#손 동작
def default_gesture(hand_landmarks):
    global previous_hand_position, previous_time, presenting_flag

    current_hand_position = calculation.get_hand_center(hand_landmarks)
    current_time = time.time()

    if previous_hand_position is None or previous_time is None:
        previous_hand_position = current_hand_position
        previous_time = current_time
        return
    
    dx = current_hand_position[0] - previous_hand_position[0]
    dy = current_hand_position[1] - previous_hand_position[1]
    dt = current_time - previous_time

    if dt > 0:  
        speed_x = dx / dt
        speed_y = dy / dt
        movement_threshold = 0.1
        speed_threshold = 0.8

    if abs(dx) > abs(dy):
        if dx > movement_threshold and speed_x > speed_threshold:
            print('The hand moved from left to right')
            custom_module.send_message("left")
            previous_hand_position = None
            previous_time = None
        elif dx < -movement_threshold and speed_x < -speed_threshold:
            print('The hand moved from right to left')
            custom_module.send_message("right")
            previous_hand_position = None
            previous_time = None
    if abs(dy) > abs(dx):
        if dy > movement_threshold and speed_y > speed_threshold:
            presenting_flag = not presenting_flag
            state = "ON" if presenting_flag else "OFF"
            print(f"Presenting: {state}")
            custom_module.send_message(state)

    previous_hand_position = current_hand_position
    previous_time = current_time

def is_pointing(hand_landmarks):
    thumb_tolerance = 0.02
    finger.load_fingers(hand_landmarks)
    if (finger.index_tip.y < finger.index_pip.y and
        finger.thumb_tip.y > (finger.thumb_ip.y - thumb_tolerance) and
        finger.middle_tip.y > finger.middle_pip.y and
        finger.ring_tip.y > finger.ring_pip.y and
        finger.pinky_tip.y > finger.pinky_pip.y):
        return True
    return False

def is_drawing(hand_landmarks):
    thumb_tolerance = 0.02
    finger.load_fingers(hand_landmarks)
    if (finger.index_tip.y < finger.index_pip.y and
        finger.middle_tip.y < finger.middle_pip.y and
        finger.thumb_tip.y > (finger.thumb_ip.y - thumb_tolerance) and
        finger.ring_tip.y > finger.ring_pip.y and
        finger.thumb_tip.y < finger.ring_tip.y and 
        finger.pinky_tip.y > finger.pinky_pip.y):
        return True
    return False

def is_stop(hand_landmarks):
    finger.load_fingers(hand_landmarks)
    middle_distance = calculation.calculate_distance(finger.middle_tip, finger.middle_dip)
    ring_distance = calculation.calculate_distance(finger.ring_tip, finger.ring_dip)
    pinky_distance = calculation.calculate_distance(finger.pinky_tip, finger.pinky_dip)
    if (finger.index_tip.y > finger.index_pip.y and 
        finger.middle_tip.y > finger.middle_pip.y and
        finger.ring_tip.y > finger.ring_pip.y and
        finger.pinky_tip.y > finger.pinky_pip.y and
        finger.thumb_tip.y < finger.middle_dip.y and
        finger.thumb_tip.y > finger.middle_pip.y and
        finger.thumb_tip.y < finger.ring_dip.y and
        finger.thumb_tip.y > finger.ring_pip.y and
        middle_distance < 0.1 and
        ring_distance < 0.1 and
        pinky_distance < 0.1):
        return True
    return False

