import cv2
import mediapipe as mp
import pyautogui

capture = cv2.VideoCapture(0)
hand_detection = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

index_trigger_y = 0
thumb_trigger_y = 0

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detection.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand_landmarks in hands:
            drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_width / frame_width * y
                    pyautogui.moveTo(middle_x, middle_y)

                if id == 6:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_trigger_x = screen_width / frame_width * x
                    index_trigger_y = screen_width / frame_width * y

                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_width / frame_width * y
                    if abs(index_y - index_trigger_y) < 15:
                        pyautogui.click()

                if id == 5:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_trigger_x = screen_width / frame_width * x
                    thumb_trigger_y = screen_width / frame_width * y

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_width / frame_width * y
                    if abs(thumb_y - thumb_trigger_y) < 5:
                        pyautogui.click(button='right')

    cv2.imshow('Cam Mouse', frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
