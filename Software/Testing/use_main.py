import cv2
import time
import math
from use_test_track import find_color_mask, find_largest_contour
from use_test_PID import PID
from use_inverse_kinematics import map_xyz_to_normal, kinema_inv
from use_test_servo import SERVO_PINS, pigpio, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH

"""
Main loop for ball balancing robot
 Detects ball position
 Computes PID control
 Uses inverse kinematics to get servo angles
 Moves servos accordingly
"""

# Initialize camera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Error: Could not open camera.")
time.sleep(2)

gains = [1.0, 0.1, 0.05]  # Tune these values for your robot
scale_factor = 1.0
filter_coeff = 0.5
pid = PID(gains, scale_factor, filter_coeff)

pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("Failed to connect to pigpio daemon.")
for pin in SERVO_PINS:
    pi.set_mode(pin, pigpio.OUTPUT)

try:
    while True:
        ret, frame = camera.read()
        if not ret or frame is None:
            print("Error: Frame not captured")
            break

        mask = find_color_mask(frame)
        x, y, radius, center = find_largest_contour(mask)

        frame_center = (frame.shape[1] // 2, frame.shape[0] // 2)
        goal = frame_center
        current_value = center

        # PID calculation
        theta, phi = pid.compute(goal, current_value)

        # Convert PID output to platform tilt (x, y)
        tilt_x = phi * math.cos(math.radians(theta)) / 100.0
        tilt_y = phi * math.sin(math.radians(theta)) / 100.0

        # Kinematics: get servo angles
        normal = map_xyz_to_normal(tilt_x, tilt_y, 0)
        Pz = 0.0632  # Platform height, tune for your robot
        servo_angles = kinema_inv(normal, Pz)

        # Move servos (mapping from angles to pulsewidths, clamped)
        for i, angle in enumerate(servo_angles):
            # Clamp angle between 0 and 180
            angle = max(0, min(180, float(angle)))
            pulsewidth = int(MIN_PULSE_WIDTH + (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH) * (angle / 180))
            pulsewidth = max(MIN_PULSE_WIDTH, min(MAX_PULSE_WIDTH, pulsewidth))
            pi.set_servo_pulsewidth(SERVO_PINS[i], pulsewidth)

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
finally:
    # Cleanup
    for pin in SERVO_PINS:
        pi.set_servo_pulsewidth(pin, 0)
    pi.stop()
    cv2.destroyAllWindows()
    camera.release()