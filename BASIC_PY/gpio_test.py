import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

p = GPIO.PWM(12, 90)
s = GPIO.PWM(32, 90)

p.start(0)
s.start(0)

try:
    while 1:
        for dc in range(0, 101, 5):
            s.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
            s.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
s.stop()
GPIO.cleanup()