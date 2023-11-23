import time
import RPi.GPIO as GPIO

def move_stop():
    right_forward.ChangeDutyCycle(0)
    right_backward.ChangeDutyCycle(0)
    left_forward.ChangeDutyCycle(0)
    left_backward.ChangeDutyCycle(0)

def move_forward(duty, time):
    right_forward.ChangeDutyCycle(duty)
    left_forward.ChangeDutyCycle(duty)
    time.sleep(time)
    right_forward.ChangeDutyCycle(0)
    left_forward.ChangeDutyCycle(0)

def move_backward(duty, time):
    right_backward.ChangeDutyCycle(duty)
    left_backward.ChangeDutyCycle(duty)
    time.sleep(time)
    right_backward.ChangeDutyCycle(0)
    left_backward.ChangeDutyCycle(0)

def spin_left(duty, time):
    right_forward.ChangeDutyCycle(duty)
    left_backward.ChangeDutyCycle(duty)
    time.sleep(time)
    right_forward.ChangeDutyCycle(0)
    left_backward.ChangeDutyCycle(0)

def spin_right(duty, time):
    right_backward.ChangeDutyCycle(duty)
    left_forward.ChangeDutyCycle(duty)
    time.sleep(time)
    right_backward.ChangeDutyCycle(0)
    left_forward.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

right_backward = GPIO.PWM(12, 90) # RIGHT BACKWARD
right_forward = GPIO.PWM(32, 90) # RIGHT FORWARD
left_forward = GPIO.PWM(33, 90) # LEFT FORWARD
left_backward = GPIO.PWM(35, 90) # LEFT BACKWARD

right_backward.start(0)
right_forward.start(0)
left_forward.start(0)
left_backward.start(0)

print("MOVING ROBOT...")

try:
    while 1:
        move_forward(90, 1)
        time.sleep(1)
        move_backward(90, 1)
        time.sleep(1)
        spin_left(90, 1)
        time.sleep(1)
        spin_right(90, 1)
        time.sleep(1)
        
except KeyboardInterrupt:
    pass
right_backward.stop()
right_forward.stop()
left_forward.stop()
left_backward.stop()
GPIO.cleanup()

