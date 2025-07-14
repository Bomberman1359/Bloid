import cv2
import numpy as np
import threading
lock = threading.Lock()


class Camera:
    def __init__(self):
        # Initialize, configure, and start the camera using OpenCV
        self.cap = cv2.VideoCapture(0)  # Open the default camera (index 0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)  # Set the width
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the height
        self.height = 480
        self.width = 480

        # Define the HSV range for fluorescent pink
        self.lower_pink = np.array([153, 50, 163])  # H: approximately from 140 degrees
        self.upper_pink = np.array([176, 112, 255])  # H: approximately up to 170 degrees

    def take_pic(self):
        # Capture a frame from the camera
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture image from camera")
        return frame

    def show_video(self, image):
        cv2.imshow("Live", image)
        cv2.waitKey(1)
    
    def find_ball(self, image):
        # Convert to HSV color space
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # Create a mask based on the color range
        mask = cv2.inRange(image_hsv, self.lower_pink, self.upper_pink)
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            # Get the minimum enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            area = cv2.contourArea(largest_contour)  # Calculate the area
            if area > 200:  # Threshold to ignore noise
                # Draw the circle on the image
                cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                self.show_video(image)
                d = radius * 2
                h = 10000 / d
                # Adjust the center
                x -= self.height / 2
                y -= self.width / 2
                x, y = -y, x
                return int(x), int(y), int(area)  # Return the coordinates and area
        self.show_video(image)
        return -1, -1, 0  # If the ball is not detected

    def clean_up_cam(self):
        self.cap.release()
        cv2.destroyAllWindows()
