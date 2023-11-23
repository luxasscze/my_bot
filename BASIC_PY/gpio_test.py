import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

p = GPIO.PWM(12, 90)
s = GPIO.PWM(32, 90)
a = GPIO.PWM(33, 90)
b = GPIO.PWM(35, 90)

p.start(0)
s.start(0)
a.start(0)
b.start(0)

print("starting motor test")

try:
    while 1:
        for dc in range(0, 101, 5):
            print("phase A")
            s.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
            print("phase B")
            s.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(0, 101, 5):
            print("phase C")
            p.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
            print("phase D")
            p.ChangeDutyCycle(dc)
            time.sleep(1)

        for dc in range(0, 101, 5):
            print("phase E")
            a.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
            print("phase F")
            a.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(0, 101, 5):
            print("phase G")
            b.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
            print("phase H")
            b.ChangeDutyCycle(dc)
            time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
s.stop()
a.stop()
b.stop()
GPIO.cleanup()