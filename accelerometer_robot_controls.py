import numpy
import scipy.special
import scipy.misc
import scipy.ndimage
from time import sleep
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

Left_Motor_Forward = 16
Left_Motor_Backward = 18

Right_Motor_Forward = 11
Right_Motor_Backward = 13

GPIO.setup(Left_Motor_Forward,GPIO.OUT)
GPIO.setup(Left_Motor_Backward,GPIO.OUT)

GPIO.setup(Right_Motor_Forward,GPIO.OUT)
GPIO.setup(Right_Motor_Backward,GPIO.OUT)

def forward():
    GPIO.output(Left_Motor_Forward,GPIO.HIGH)
    GPIO.output(Left_Motor_Backward,GPIO.LOW)

    GPIO.output(Right_Motor_Forward,GPIO.HIGH)
    GPIO.output(Right_Motor_Backward,GPIO.LOW)

def backward():
    GPIO.output(Left_Motor_Forward,GPIO.LOW)
    GPIO.output(Left_Motor_Backward,GPIO.HIGH)

    GPIO.output(Right_Motor_Forward,GPIO.LOW)
    GPIO.output(Right_Motor_Backward,GPIO.HIGH)

def right():
    GPIO.output(Left_Motor_Forward,GPIO.HIGH)
    GPIO.output(Left_Motor_Backward,GPIO.LOW)

    GPIO.output(Right_Motor_Forward,GPIO.LOW)
    GPIO.output(Right_Motor_Backward,GPIO.LOW)

def left():
    GPIO.output(Left_Motor_Forward,GPIO.LOW)
    GPIO.output(Left_Motor_Backward,GPIO.HIGH)

    GPIO.output(Right_Motor_Forward,GPIO.LOW)
    GPIO.output(Right_Motor_Backward,GPIO.LOW)

def stop():
    GPIO.output(Left_Motor_Forward,GPIO.LOW)
    GPIO.output(Left_Motor_Backward,GPIO.LOW)

    GPIO.output(Right_Motor_Forward,GPIO.LOW)
    GPIO.output(Right_Motor_Backward,GPIO.LOW)

while True:
    accelerometerdata = open('accelerometerdata.txt')
    data = accelerometerdata.readlines()
    if not data:
        continue
    x_coordinate = data[0]
    y_coordinate = data[1]
    z_coordinate = data[2]
    x_coordinate = float(x_coordinate)
    y_coordinate = float(y_coordinate)
    z_coordinate = float(z_coordinate)
    print(x_coordinate, y_coordinate, z_coordinate)
    accelerometerdata.close

    if y_coordinate <=-4:
        forward()
        print('forward')

    elif y_coordinate >4:
        backward()
        print('backward')

    elif x_coordinate <= -4:
        right()
        print('right')

    elif x_coordinate >4:
        left()
        print('left')

    else:
        stop()
        print('stop')

GPIO.cleanup()
