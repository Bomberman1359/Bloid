import pigpio
import time

SERVO_PINS = [17, 18, 22]
MIN_PULSE_WIDTH = 1500   # ~0 degrees

def set_servos_to_zero():
    pi = pigpio.pi()
    if not pi.connected:
        print("Failed to connect to pigpio daemon.")
        return

    try:
        while True:
            for pin in SERVO_PINS:
                pi.set_mode(pin, pigpio.OUTPUT)
                pi.set_servo_pulsewidth(pin, MIN_PULSE_WIDTH)
            time.sleep(0.01)  # Repeat quickly
    finally:
        for pin in SERVO_PINS:
            pi.set_servo_pulsewidth(pin, 0)
        pi.stop()

if __name__ == "__main__":
    set_servos_to_zero()
