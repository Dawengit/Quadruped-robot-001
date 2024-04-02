# extreme position test
# Dawen Huang
# 2024/03/27

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

# There should 8 servos connected, with IDs 1, 2, 3, 4，5, 6, 7, 8
try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
    servo8 = LX16A(8)

except ServoTimeoutError:
    print('Servo is not responding. Exiting.')
    exit()

print(servo1.get_physical_angle())
print(servo2.get_physical_angle())
print(servo3.get_physical_angle())
print(servo4.get_physical_angle())
print(servo5.get_physical_angle())
print(servo6.get_physical_angle())
print(servo7.get_physical_angle())
print(servo8.get_physical_angle())