import RPi.GPIO as GPIO
import spidev
import time

# Pin config
RST_PIN = 5
DC_PIN = 16
CS_PIN = 8
BUSY_PIN = 9

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RST_PIN, GPIO.OUT)
GPIO.setup(DC_PIN, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT)
GPIO.setup(BUSY_PIN, GPIO.IN)

# SPI setup
spi = spidev.SpiDev(0, 0)
spi.max_speed_hz = 2000000

def digital_write(pin, value):
    GPIO.output(pin, value)

def digital_read(pin):
    return GPIO.input(pin)

def delay(ms):
    time.sleep(ms / 1000.0)

def send_command(command):
    digital_write(DC_PIN, 0)
    digital_write(CS_PIN, 0)
    spi.writebytes([command])
    digital_write(CS_PIN, 1)

def send_data(data):
    digital_write(DC_PIN, 1)
    digital_write(CS_PIN, 0)
    spi.writebytes([data])
    digital_write(CS_PIN, 1)

def wait_until_idle():
    while digital_read(BUSY_PIN) == 1:
        delay(10)

def reset():
    digital_write(RST_PIN, 0)
    delay(200)
    digital_write(RST_PIN, 1)
    delay(200)

def init():
    reset()
    wait_until_idle()
    
    send_command(0x01)  # POWER_SETTING
    send_data(0x03)
    send_data(0x00)
    send_data(0x2b)
    send_data(0x2b)
    
    send_command(0x06)  # BOOSTER_SOFT_START
    send_data(0x17)
    send_data(0x17)
    send_data(0x17)

    send_command(0x04)  # POWER_ON
    wait_until_idle()

    send_command(0x00)  # PANEL_SETTING
    send_data(0xBF)     # LUT from OTP, B/W mode
    send_data(0x0D)

    send_command(0x30)  # PLL_CONTROL
    send_data(0x3A)

    send_command(0x61)  # RESOLUTION
    send_data(0xFA)     # 250
    send_data(0x00)     
    send_data(0x7A)     # 122

    send_command(0x82)  # VCOM_DC_SETTING
    send_data(0x12)

def display_image(image_data):
    # Assumes image_data is 250*122 bits (3832 bytes)
    send_command(0x10)
    for b in image_data:
        send_data(b)

    send_command(0x12)  # DISPLAY_REFRESH
    wait_until_idle()

def clear():
    send_command(0x10)
    for _ in range(250 * 122 // 8):
        send_data(0xFF)  # white

    send_command(0x12)
    wait_until_idle()

def sleep():
    send_command(0x02)  # POWER_OFF
    wait_until_idle()
    send_command(0x07)
    send_data(0xA5)

def main():
    try:
        init()
        clear()
        delay(1000)

        # Draw checkerboard pattern
        buffer = []
        for y in range(122):
            for x in range(250 // 8):
                if (x + y) % 2 == 0:
                    buffer.append(0x00)  # black
                else:
                    buffer.append(0xFF)  # white

        display_image(buffer)
        delay(5000)
        sleep()

    finally:
        spi.close()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
