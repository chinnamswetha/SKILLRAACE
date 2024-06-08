import cv2
import numpy as np
import pyautogui

# Screen resolution
screen_width, screen_height = pyautogui.size()

# Define codec and create video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_width, screen_height))

while True:
    # Capture screenshot
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Write frame to video file
    out.write(frame)

    # Check for exit condition
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video writer and close windows
out.release()
cv2.destroyAllWindows()