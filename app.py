import cv2
import mediapipe as mp
import pyautogui

# Open cam for the recognition
capture = cv2.VideoCapture(0)
# Set the frame width and height for faster processing
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# Initialize hand detection
hand_detection = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
# Utility functions for drawing landmarks on the frame. The one with the circles for the hand
drawing_utils = mp.solutions.drawing_utils
# Get the screen size for accurate cursor movements
screen_width, screen_height = pyautogui.size()

#The trigger variables are for the event detections when the landmarks collide

# Initialize the trigger y-coordinate for the middle finger.
middle_trigger_y = 0
middle_finger_tip_y = 0
# Initialize the trigger y-coordinate for the thumb
thumb_trigger_y = 0
thumb_finger_tip_y = 0

# Pre calculate the screen ratio width to frame for complicated reasons
width_ratio = screen_width / capture.get(cv2.CAP_PROP_FRAME_WIDTH)

def process_landmark(id, x, y):
    global middle_trigger_y,middle_finger_tip_y, thumb_trigger_y, thumb_finger_tip_y
    
    #initiate x and y coordinates for the drawing of circles
    circle_x = x
    circle_y = y
    
    # Scale the x and y coords based on the screen width to frame width ratio
    x = width_ratio * x
    y = width_ratio * y

    if id == 8:
        # Draw circle on the frame at the landmark position
        cv2.circle(img=frame, center=(circle_x,circle_y), radius=10, color=(0,255,255))
        # Move the mouse to the tip of the index finger
        pyautogui.moveTo(x, y)
    if id == 10:
        # Draw circle on the frame at the landmark position
        cv2.circle(img=frame, center=(circle_x,circle_y), radius=10, color=(0,255,255))
        # Update the trigger y coords for the middle finger
        middle_trigger_y = y
    if id == 12:
        # Draw circle on the frame at the landmark position
        cv2.circle(img=frame, center=(circle_x,circle_y), radius=10, color=(0,255,255))
        # Update the trigger y coords for the middle finger tip
        middle_finger_tip_y = y
        if abs(middle_finger_tip_y - middle_trigger_y) < 20:
            # Perform a left click if the middle finger is close to the trigger position
            pyautogui.click()
            pyautogui.sleep(0.3)
    if id == 5:
        # Draw circle on the frame at the landmark position
        cv2.circle(img=frame, center=(circle_x,circle_y), radius=10, color=(0,255,255))
        # Update the trigger y-coordinate for the thumb
        thumb_trigger_y = y
    if id == 4:
        # Draw circle on the frame at the landmark position
        cv2.circle(img=frame, center=(circle_x,circle_y), radius=10, color=(0,255,255))
        # Update the trigger y-coordinate for the thumb finger tip
        thumb_finger_tip_y = y
        if abs(thumb_finger_tip_y - thumb_trigger_y) < 10:
            # Perform a right click if the thumb is close to the trigger position
            pyautogui.click(button="right")
            pyautogui.sleep(0.3)
        

while True:
    # Read a frame from the cam
    ret, frame = capture.read()
    if not ret:
        break
    # Flip the cam horizontally for accurate trigger position
    frame = cv2.flip(frame, 1)
    # Get the height and width of the frame
    frame_height, frame_width, _ = frame.shape
    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame to detect hand landmarks (circles)
    output = hand_detection.process(rgb_frame)
    # Get the detected hand landmarks
    hands = output.multi_hand_landmarks

    if hands:
        for hand_landmarks in hands:
            # Draw the hand landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            # Get the individual landmarks of the hand
            landmarks = hand_landmarks.landmark
            for id, landmark in enumerate(landmarks):
                # Calculate the x-coordinate of the landmark in the frame
                x = int(landmark.x * frame_width)
                # Calculate the y-coordinate of the landmark in the frame
                y = int(landmark.y * frame_height)
                # Process the landmark
                process_landmark(id, x, y)

    # Display the frame with the hand landmarks
    cv2.imshow('Navi Preview', frame)

    cv2.waitKey(1)

# release webcam
capture.release()
# Close all windows
cv2.destroyAllWindows()
