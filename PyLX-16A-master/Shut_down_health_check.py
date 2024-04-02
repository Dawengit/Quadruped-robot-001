#from lx16a import *
from lx16a import *
from math import sin, cos
import time
# This is the port that the controller board is connected to
# # This will be different for different computers Raspbian
# # On Windows, try the ports COM1, COM2, COM3, etc...
# # On , try each port in /dev/

port = 'COM7'
LX16A.initialize(port)
# LX16A.initialize("/dev/ttyUSB0", 0.1)
# There should four servos connected, with IDs 1, 2, 3, 4，5, 6, 7, 8
try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
except ServoTimeoutError:
    print('Servo is not responding. Exiting.')
    exit()

def healthCheck():
    # query servo positions
    try:
        x1 = servo1.get_physical_angle()
        x2 = servo2.get_physical_angle()
        x3 = servo3.get_physical_angle()
        x4 = servo4.get_physical_angle()
    except ServoTimeoutError:
        print('Servo is not responding. Exiting.')
        exit()

    # query voltage inputs to each servo
    v1 = servo1.get_vin()
    v2 = servo1.get_vin()
    v3 = servo1.get_vin()
    v4 = servo1.get_vin()
    print(v1, v2, v3, v4)

    # flash servo LEDs 3 times to confirm health check complete
    for i in range(3):
        servo1.led_power_on()
        time.sleep(0.1)
        servo1.led_power_off()
        time.sleep(0.1)

    for i in range(3):
        servo2.led_power_on()
        time.sleep(0.1)
        servo2.led_power_off()
        time.sleep(0.1)

    for i in range(3):
        servo3.led_power_on()
        time.sleep(0.1)
        servo3.led_power_off()
        time.sleep(0.1)

    for i in range(3):
        servo4.led_power_on()
        time.sleep(0.1)
        servo4.led_power_off()
        time.sleep(0.1)