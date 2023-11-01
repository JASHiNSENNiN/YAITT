# Hand Navi

Hand Navi is a Python script that allows you to control your computer's mouse cursor and perform left and right clicks using hand gestures captured by your webcam. It utilizes the Mediapipe library for hand detection and OpenCV for image processing.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## Usage

1. Connect a webcam to your computer.
2. Run the script using the command `python cam_mouse.py`.
3. A window will open showing the webcam feed with hand landmarks.
4. Move your hand in front of the webcam to control the mouse cursor.
5. Perform the following gestures to control the mouse:

   - Index Finger: Move the mouse cursor to the tip of the index finger.
   - Middle Finger: Bring the middle finger close to the trigger position to perform a left click.
   - Thumb: Bring the thumb close to the trigger position to perform a right click.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [Mediapipe](https://mediapipe.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)

## Author
[JASHiN](https://github.com/JASHiNSENNiN)
