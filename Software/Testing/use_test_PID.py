import math
import time


class PID:
    def __init__(self, gains, scale_factor, filter_coeff):
        self.kp = gains[0]
        self.ki = gains[1]
        self.kd = gains[2]
        self.scale_factor = scale_factor
        self.filter_coeff = filter_coeff  # Coefficient for low-pass filter
        self.prev_filtered_x = 0
        self.prev_filtered_y = 0
        self.prev_error_x = 0
        self.integral_x = 0
        self.prev_error_y = 0
        self.integral_y = 0
        self.prev_time = None

    def compute(self, target, current):
        now = time.perf_counter()
        if self.prev_time is None:
            self.prev_time = now
            return 0, 0
        # Calculate error
        error_x = target[0] - current[0]
        error_y = target[1] - current[1]
        # Calculate integral value
        dt = now - self.prev_time
        self.integral_x += error_x * dt
        self.integral_y += error_y * dt
        # Calculate derivative value
        derivative_x = (error_x - self.prev_error_x) / dt
        derivative_y = (error_y - self.prev_error_y) / dt
        # Calculate PID output
        raw_output_x = self.kp * error_x + self.ki * self.integral_x + self.kd * derivative_x
        raw_output_y = self.kp * error_y + self.ki * self.integral_y + self.kd * derivative_y
        # Apply low-pass filter
        filtered_x = self.filter_coeff * raw_output_x + (1 - self.filter_coeff) * self.prev_filtered_x
        filtered_y = self.filter_coeff * raw_output_y + (1 - self.filter_coeff) * self.prev_filtered_y
        # Calculate direction (angle) and magnitude
        angle_deg = math.degrees(math.atan2(filtered_y, filtered_x))
        if angle_deg < 0:
            angle_deg += 360
        magnitude = self.scale_factor * math.sqrt(filtered_x**2 + filtered_y**2)

        self.prev_error_x = error_x
        self.prev_error_y = error_y
        self.prev_filtered_x = filtered_x
        self.prev_filtered_y = filtered_y
        self.prev_time = now

        return angle_deg, magnitude