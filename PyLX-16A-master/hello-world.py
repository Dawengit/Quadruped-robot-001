from math import sin, cos
from lx16a import *

import time

LX16A.initialize("com7", 0.1)

def servo_info(id):
    print("Servo id: {}".format(id))
    print("Position: {}".format(ctrl.get_position(id)))
    print("Temperature: {}, limit: {}".format(ctrl.get_temperature(id), ctrl.get_max_temperature_limit(id)))
    print("Led error: {}".format(ctrl.get_led_errors(id)))

try:
    servo1 = LX16A(7)
    servo2 = LX16A(8)
    # set angle limit
    # for one leg there's two motors. upper motor(1), down motor(2)
    servo1.set_angle_limits(0, 120)
    servo2.set_angle_limits(0, 120)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()



t = 0
while True:
    servo1.move(sin(t) * 60 + 60)
    servo2.move(cos(t) * 60 + 60)

    time.sleep(0.05)
    t += 0.1

#from lx16a import *
# from lx16a import *
# from math import sin, cos
# import time
# This is the port that the controller board is connected to
# # This will be different for different computers Raspbian
# # On Windows, try the ports COM1, COM2, COM3, etc...
# # On , try each port in /dev/


# def move_servo(ser, angle):
#     ser = LX16A(1)
#     step = (angle - ser.get_physical_angle()) / 10
#     for i in range(10):
#         ser.move(step)
#         time.sleep(0.1)



# port = 'COM7'
# LX16A.initialize(port)


# # There should two servos connected, with IDs 1 and 2
# try:
#     servo1 = LX16A(1)
#     servo2 = LX16A(2)
#     servo3 = LX16A(3)
#     servo4 = LX16A(4)
# except ServoTimeoutError:
#     print('Servo is not responding. Exiting.')
#     exit()

# home1 = 132.48
# home2 = 138.0
# home3 = 141.84
# home4 = 154.08

# servo1.set_angle_limits(home1-60, home1+60)
# servo2.set_angle_limits(home2-60, home2+60)
# servo3.set_angle_limits(home3-60, home3+60)
# servo4.set_angle_limits(home4-60, home4+60)


# # move_servo(servo1, home1)
# # move_servo(servo2, home2)
# # move_servo(servo3, home3)
# # move_servo(servo4, home4)
# time.sleep(2)

# t = 0
# while True:
#     # Two sine waves out of phase
#     servo1.move(home1+sin(t)*20)
#     servo2.move(home2+sin(t)*20)
#     servo3.move(home3+sin(t)*20)
#     servo4.move(home4+sin(t)*20)

#     time.sleep(0.05)
#     t += 0.05


