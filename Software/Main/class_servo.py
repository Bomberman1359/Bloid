import pigpio
import time

class RS304MD:
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise RuntimeError("Failed to connect to pigpio daemon")
        # Set the GPIO pin as an output
        self.pi.set_mode(self.gpio_pin, pigpio.OUTPUT)

    # Method to set the servo angle
    def control_rotate(self, angle):
        # Convert angle to pulse width (1000-2000 microseconds for 0-180 degrees)
        pulse_width = int(1000 + (angle / 180.0) * 1000)
        self.pi.set_servo_pulsewidth(self.gpio_pin, pulse_width)

    # Method to set the servo angle with a specified time (not directly supported in pigpio)
    def control_time_rotate(self, angle, t):
        self.control_rotate(angle)
        time.sleep(t)

    # Method to turn off the servo (stop sending PWM signal)
    def trq_set(self, status):
        if status == 0:  # Turn off torque
            self.pi.set_servo_pulsewidth(self.gpio_pin, 0)

    # Cleanup method to stop pigpio
    def cleanup(self):
        self.pi.stop()