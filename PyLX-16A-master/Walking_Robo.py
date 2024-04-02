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
    servo8 = LX16A(8) 
    
except ServoTimeoutError:
    print('Servo is not responding. Exiting.')
    exit()
############################################################################################################
# Initialize servos
# SET HOME POSITIONS
    # The first home strategy is for the robot's legs to be in four corners of a square
    # The second home strategy is for the robot's legs to be in a straight line
# leg1
home1 = 110.0+5
#home2 = 82
# leg2
home3 = 140.0
#home4 = 85.0
# leg3
home5 = 235.0
#home6 = 144.0
# leg4
home7 = 80.0+5
#home8 = 73.0

# SET ANGLE LIMITS
# leg1
servo1.set_angle_limits(110,184)
servo2.set_angle_limits(82,134)
#home2=(134+82)/2=108
home2=(134+82)/2
# leg2
servo3.set_angle_limits(76, 148)
servo4.set_angle_limits(27, 85)
# home4=(27+85)/2=56
home4=(27+85)/2

# leg3
servo5.set_angle_limits(166, 240)
servo6.set_angle_limits(87,144)
# home6=(87+144)/2=115.5
home6=(87+144)/2

# leg4
servo7.set_angle_limits(80,160)
servo8.set_angle_limits(73,127)
# home8=(73+127)/2=100
home8=(73+127)/2

# MOVE SERVOS TO HOME POSITIONS

servo1.move(home1)
servo2.move(home2)
servo3.move(home3)
servo4.move(home4)
servo5.move(home5)
servo6.move(home6)
servo7.move(home7)
servo8.move(home8)

# Gait coding
# One cycle of gait
# 1. move leg 1 and leg 4
# move leg 1 backward and leg 4 forward
# leg1 position 1 (home) to position 2a (servo1, servo2)= (110, 82) to (115, 134)
# leg4 position 1 (home) to position 2d (servo7, servo8)= (80, 73) to (85, 127)

# 2. move leg 2 and leg 3 
# move leg 2 backward and leg 3 forward
# leg2 position 1 (home) to position 2b (servo3, servo4)= (140, 85) to (135, 27)
# leg3 position 1 (home) to position 2c (servo5, servo6)= (240,144) to (240, 87)

# 3. move leg 1 and leg 4
# move leg 1 forward and leg 4 backward
# leg1 position 2a (servo1, servo2) to position 1 (home)= (115, 134) to (110, 82)
# leg4 position 2d (servo7, servo8) to position 1 (home)= (85, 127) to (80, 73)

# 4. move leg 2 and leg 3
# move leg 2 forward and leg 3 backward
# leg2 position 2b (servo3, servo4) to position 1 (home)= (135, 27) to (140, 85)
# leg3 position 2c (servo5, servo6) to position 1 (home)= (240, 87) to (240, 144)
t=0
while True:
    # 1. move leg 1 and leg 4
    # move leg 1 backward and leg 4 forward
    # apply sin and cos to make smooth movement to goal position
    servo1.move(home1+sin(t)*3)
    servo2.move(home2-sin(t)*((134-82)/2-15))
    servo7.move(home7+sin(t)*3)
    servo8.move(home8+sin(t)*((127-73)/2-15))

    time.sleep(0.05)
    # 2. move leg 2 and leg 3 9
    # move leg 2 backward and leg 3 forward
    servo3.move(home3+sin(t)*3)
    servo4.move(home4+sin(t)*((27-85)/2+15))
    servo5.move(home5+sin(t)*3)
    servo6.move(home6-sin(t)*((87-144)/2+15))

    time.sleep(0.05)
    t=t+0.05





# # move_servo to home position
# time.sleep(2)

# t = 0
# while True:
#     # Two sine waves out of phase
#     servo1.move(home1+sin(t)*20)
#     servo2.move(home2+sin(t)*20)
#     servo3.move(home3+sin(t)*20)
#     servo4.move(home4+sin(t)*20)
#     servo5.move(home5+sin(t)*20)
#     servo6.move(home6+sin(t)*20)
#     servo7.move(home7+sin(t)*20)
#     servo8.move(home8+sin(t)*20)

#     time.sleep(0.05)
#     t += 0.05


# def calcStep1(curr, goal, ts):
#     step = (goal-curr)/ts
#     for i in range(0,ts):
#         servo1.move(curr+step)
#         curr = servo1.get_physical_angle()
#         time.sleep(gts)

# def calcStep2(curr, goal, ts):
#     step = (goal-curr)/ts
#     for i in range(0,ts):
#         servo2.move(curr+step)
#         curr = servo2.get_physical_angle()
#         time.sleep(gts)

# def calcStep3(curr, goal, ts):
#     step = (goal-curr)/ts
#     for i in range(0,ts):
#         servo3.move(curr+step)
#         curr = servo3.get_physical_angle()
#         time.sleep(gts)

# def calcHips(curr1, goal1, curr2, goal2, ts):
#     step1 = (goal1 - curr1) / ts
#     step2 = (goal2 - curr2) / ts
#     for i in range(0, ts):
#         servo2.move(curr1 + step1)
#         curr1 = servo2.get_physical_angle()
#         servo3.move(curr2 + step2)
#         curr2 = servo3.get_physical_angle()
#         time.sleep(gts)

# def calcStep4(curr, goal, ts):
#     step = (goal-curr)/ts
#     for i in range(0,ts):
#         servo4.move(curr+step)
#         curr = servo4.get_physical_angle()
#         time.sleep(gts)


# time.sleep(2)

# t = 0


# t = 15

# while True:
#     # lift leg
#     calcStep1(servo1.get_physical_angle(), 230, t)
#     calcStep4(servo4.get_physical_angle(), 100, t)

#     calcStep3(servo3.get_physical_angle(), 70, t)

#     calcStep4(servo4.get_physical_angle(), 65, t)
#     calcHips(servo2.get_physical_angle(), 30, servo3.get_physical_angle(), 30, 20)

#     # foot down
#     calcStep4(servo4.get_physical_angle(), 170, t)  # NOTE: changed from 190, 90
#     calcStep1(servo1.get_physical_angle(), 110, t)
#     time.sleep(0.5)

#     #reset
#     calcStep4(servo4.get_physical_angle(), 175, t)
#     calcHips(servo2.get_physical_angle(), 220, servo3.get_physical_angle(), 220, 20)

#     servo1.move(home1)
#     servo2.move(home2)
#     servo3.move(home3)
#     servo4.move(home4)

#     time.sleep(0.5)

#     calcStep4(servo4.get_physical_angle(), 56, t)
#     calcStep1(servo1.get_physical_angle(), 186, t)

#     calcStep2(servo2.get_physical_angle(), 210, t)

#     calcStep1(servo1.get_physical_angle(), 220, t)
#     # calcStep1(servo1.get_physical_angle(), 240, t)
#     # pause


#     calcHips(servo2.get_physical_angle(), 250, servo3.get_physical_angle(), 250, 20)

#     calcStep1(servo1.get_physical_angle(), 110, t)
#     calcStep4(servo4.get_physical_angle(), 170, t)

#     calcStep1(servo1.get_physical_angle(), 100, t)  # changed from 115
#     calcHips(servo2.get_physical_angle(), 60, servo3.get_physical_angle(), 60, 20)

#     servo1.move(home1)
#     servo2.move(home2)
#     servo3.move(home3)
#     servo4.move(home4)

#     time.sleep(0.5)

# # pause
# # calcStep1(servo1.get_physical_angle(), 210, t)
# #
# # calcHips(servo2.get_physical_angle(), 270, servo3.get_physical_angle(), 270, 20)
# # calcStep1(servo1.get_physical_angle(), 100, t)
# # calcStep4(servo4.get_physical_angle(), 180, t)
# # pause

# # calcHips(servo2.get_physical_angle(), 70, servo3.get_physical_angle(), 70, 10)
# # time.sleep(0.1)


# # calcStep3(servo3.get_physical_angle(), 80, t)
# # calcStep2(servo2.get_physical_angle(), 80, t)
# # calcStep3(servo3.get_physical_angle(), 100, t)

# while False:
#     #shuffle
#     calcStep1(servo1.get_physical_angle(), 190, t)
#     # calcStep2(servo2.get_physical_angle(), 92, t)
#     # calcHips(servo2.get_physical_angle(), 62, servo3.get_physical_angle(), 107, t)
#     calcStep1(servo1.get_physical_angle(), 100, t)
#     #
#     # calcStep4(servo4.get_physical_angle(), 125, t)
#     # calcStep2(servo2.get_physical_angle(), 160, t)
#     # calcHips(servo2.get_physical_angle(), 120, servo3.get_physical_angle(), 180, t)
#     # calcStep4(servo4.get_physical_angle(), 170, t )