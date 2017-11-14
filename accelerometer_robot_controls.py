import numpy
import scipy.special
import scipy.misc
import scipy.ndimage
from time import sleep
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
 
Motor1A = 16
Motor1B = 18
 
Motor2A = 11
Motor2B = 13

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
 
def forward():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
 
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
 
def backward():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)

def right():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)

def left():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
 
def stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)

##right()
##time.sleep(2)
##left()
##time.sleep(2)
##stop()
    
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


