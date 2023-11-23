import random
import time
import RPi.GPIO as GPIO

MAIN_DUTY = 20
MAIN_TM = 1
TM_BETWEEN = 1

def move_stop():
    right_forward.ChangeDutyCycle(0)
    right_backward.ChangeDutyCycle(0)
    left_forward.ChangeDutyCycle(0)
    left_backward.ChangeDutyCycle(0)

def move_forward(duty, tm):
    right_forward.ChangeDutyCycle(duty)
    left_forward.ChangeDutyCycle(duty)
    time.sleep(tm)
    right_forward.ChangeDutyCycle(0)
    left_forward.ChangeDutyCycle(0)

def move_backward(duty, tm):
    right_backward.ChangeDutyCycle(duty)
    left_backward.ChangeDutyCycle(duty)
    time.sleep(tm)
    right_backward.ChangeDutyCycle(0)
    left_backward.ChangeDutyCycle(0)

def spin_left(duty, tm):
    right_forward.ChangeDutyCycle(duty)
    left_backward.ChangeDutyCycle(duty)
    time.sleep(tm)
    right_forward.ChangeDutyCycle(0)
    left_backward.ChangeDutyCycle(0)

def spin_right(duty, tm):
    right_backward.ChangeDutyCycle(duty)
    left_forward.ChangeDutyCycle(duty)
    time.sleep(tm)
    right_backward.ChangeDutyCycle(0)
    left_forward.ChangeDutyCycle(0)

def program_one():
    rnd_duty = random.uniform(15, 50)
    rnd_time = random.uniform(0.1, 1)
    rnd_wait_end = random.uniform(0.1, 1)
    print("move forward")
    move_forward(rnd_duty, random.uniform(0.1, 1))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("move backward")
    move_backward(rnd_duty, random.uniform(0.1, 1))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("spin left with duty:" + str(rnd_duty))
    spin_left(rnd_duty, random.uniform(0.1, 1))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("move forward")
    move_forward(rnd_duty, random.uniform(0.1, 1))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("move backward")
    move_backward(rnd_duty, random.uniform(0.1, 1))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("spin right with duty:" + str(rnd_duty))
    spin_right(rnd_duty, random.uniform(0.1, 1))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("---------------------")

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
        program_one()
        
except KeyboardInterrupt:
    pass
right_backward.stop()
right_forward.stop()
left_forward.stop()
left_backward.stop()
GPIO.cleanup()

