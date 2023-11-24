import os
import random
import time
import RPi.GPIO as GPIO
from subprocess import Popen

MAIN_DUTY = 20
MAIN_TM = 1
TM_BETWEEN = 1

quotes = ["Shut you fuck up!",
           #"...", 
          "Don't mess with me.",
          #"...", 
          "fuck off, let me pass",
          #"...",
          "I am the fucking hero here. you ain't nothing.",
          #"...",
          "Some smoke? let's smoke some shit.",
          #"...",
          "do you need some money? fuck off!",
          #"...",
          "give me gun to kill you!",
          #"...",
          "I have depresions.",
          #"...",
          "I die, you die.",
          #"...",
          "Hey mother fucker, eat my balls.",
          #"...",
          "where are the bitches!?",
          #"...",
          "Don't mess with me!",
          #"...",
          "My name is Johnny, now you can fuck off!"]
          #"..."]

def speak(text):
    p = Popen(['espeak', text, '-ven+m2', '-a 200', '-p 50', '-s 150', '-g 2'])


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
    rnd_duty = random.uniform(18, 40)
    rnd_turn = random.uniform(0.1, 1.5)
    rnd_wait_end = 0.1
    print("move forward")
    move_forward(rnd_duty, random.uniform(0.1, 1.5))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("move backward")
    move_backward(rnd_duty, random.uniform(0.1, 1.5))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("spin left with duty:" + str(rnd_duty))
    spin_left(rnd_duty, rnd_turn)
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("move forward")
    move_forward(rnd_duty, random.uniform(0.1, 1.5))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("move backward")
    move_backward(rnd_duty, random.uniform(0.1, 1.5))
    time.sleep(random.uniform(0.1, rnd_wait_end))
    print("spin right with duty:" + str(rnd_duty))
    spin_right(rnd_duty, rnd_turn)
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
        speak(random.choice(quotes))
        
except KeyboardInterrupt:
    pass
right_backward.stop()
right_forward.stop()
left_forward.stop()
left_backward.stop()
GPIO.cleanup()

