import numpy as np
import cv2
import time

pinkLower = (140,  50,  50)
pinkUpper = (174, 255, 255)
"""
Ball tracking functions for use in main.py
"""

# Initialize the camera using cv2.VideoCapture

#Returns a mask of all colors within the red HSV space
def find_color_mask(frame):
	"""
	Blur the image, convert to HSV, and return mask for pink color.
	"""
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, pinkLower, pinkUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	return mask

# Finds the largest "blob" on the screen
def find_largest_contour(mask):
	"""
	Finds contours in the mask and returns the largest one's position, radius, and center.
	"""
	cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	else:
		(x, y) = (0, 0)
		radius = 5
		center = (0, 0)
	return x, y, radius, center


# This file only provides ball tracking functions for use in main.py