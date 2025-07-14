import pigpio
import time
import math

# Servo setup
SERVO_PINS = [17, 18, 22]  # 3 servos
MIN_PULSE = 500
MAX_PULSE = 2500
MID_PULSE = 1500
PULSE_RANGE = MAX_PULSE - MIN_PULSE

# Geometry
PLATFORM_RADIUS = 5.0  # cm, radius of the triangle
ARM_LENGTH = 10.0      # cm, length of each servo arm

# Convert angle to pulsewidth (for standard servo 0-180 deg)
def angle_to_pulse(angle_deg):
    pulse = MIN_PULSE + (angle_deg / 180.0) * PULSE_RANGE
    return max(MIN_PULSE, min(MAX_PULSE, pulse))

# Rotation matrix for platform tilt
def compute_platform_heights(pitch_deg, roll_deg):
    pitch = math.radians(pitch_deg)
    roll = math.radians(roll_deg)

    # Positions of 3 platform points (triangle)
    points = [
        [PLATFORM_RADIUS, 0],                          # Point 1
        [-PLATFORM_RADIUS / 2, PLATFORM_RADIUS * math.sqrt(3)/2],  # Point 2
        [-PLATFORM_RADIUS / 2, -PLATFORM_RADIUS * math.sqrt(3)/2], # Point 3
    ]

    heights = []
    for x, y in points:
        z = math.sin(pitch) * y + math.sin(roll) * x  # linear approximation
        heights.append(z)

    return heights

# Main function to set servo angles based on platform orientation
def set_platform_orientation(pi, pitch, roll):
    heights = compute_platform_heights(pitch, roll)

    for i in range(3):
        # Assume direct mapping: height → servo angle
        # Scale height to angle between 90 ± 30 degrees
        angle = 90 + heights[i] * 3  # tune this factor experimentally
        pulse = angle_to_pulse(angle)
        pi.set_servo_pulsewidth(SERVO_PINS[i], pulse)

# Example sweep (balance platform around X and Y)
def balance_loop():
    pi = pigpio.pi()
    if not pi.connected:
        print("Cannot connect to pigpio")
        return

    try:
        for pin in SERVO_PINS:
            pi.set_mode(pin, pigpio.OUTPUT)

        while True:
            # Example: oscillate platform for testing
            for deg in range(-10, 11, 2):
                set_platform_orientation(pi, pitch=deg, roll=-deg)
                time.sleep(0.05)
            for deg in range(10, -11, -2):
                set_platform_orientation(pi, pitch=deg, roll=-deg)
                time.sleep(0.05)
    finally:
        for pin in SERVO_PINS:
            pi.set_servo_pulsewidth(pin, 0)
        pi.stop()

if __name__ == "__main__":
    balance_loop()
