# code for AEB of the robot
# 
from time import sleep
from gpiozero import DistanceSensor
from lx16a import *
from Shut_down_health_check import healthcheck
# import RPi.GPIO as GPIO

def aeb():
    dis = DistanceSensor(14, 15)    #define the GPIO pins for the ultrasonic sensor
    print('', dis.distance, 'm')
    sleep(0.01)
    while dis.distance < 0.5:    #if the distance is less than 0.5m, the robot will stop (units in meters)
        print('STOP the movement of the robot')
        ## run shutdown code here
        healthcheck()
        sleep(0.01)




