#!/usr/bin/env python3

# motor_control_node.py
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
from rclpy.node import Node
import rclpy

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        GPIO.setmode(GPIO.BOARD)

        # Set up GPIO pins for motor control
        self.pin_motor1_forward = 12  # Replace with the actual GPIO pin
        self.pin_motor1_backward = 32  # Replace with the actual GPIO pin
        self.pin_motor2_forward = 33  # Replace with the actual GPIO pin
        self.pin_motor2_backward = 35  # Replace with the actual GPIO pin

        GPIO.setup(self.pin_motor1_forward, GPIO.OUT)
        GPIO.setup(self.pin_motor1_backward, GPIO.OUT)
        GPIO.setup(self.pin_motor2_forward, GPIO.OUT)
        GPIO.setup(self.pin_motor2_backward, GPIO.OUT)

        # Set up PWM for motor control
        self.pwm_motor1_forward = GPIO.PWM(self.pin_motor1_forward, 90)  # 90 Hz frequency
        self.pwm_motor1_backward = GPIO.PWM(self.pin_motor1_backward, 90)
        self.pwm_motor2_forward = GPIO.PWM(self.pin_motor2_forward, 90)
        self.pwm_motor2_backward = GPIO.PWM(self.pin_motor2_backward, 90)

        self.pwm_motor1_forward.start(0)  # Start with 0% duty cycle (stopped)
        self.pwm_motor1_backward.start(0)
        self.pwm_motor2_forward.start(0)
        self.pwm_motor2_backward.start(0)

        # Create a subscriber to receive velocity commands
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )
        self.subscription

    def cmd_vel_callback(self, msg):
        linear_vel = msg.linear.x
        angular_vel = msg.angular.z

        # Motor control logic based on linear and angular velocities
        left_motor_speed = linear_vel - angular_vel
        right_motor_speed = linear_vel + angular_vel

        # Set the duty cycle for each motor based on the speed
        self.pwm_motor1_forward.ChangeDutyCycle(max(0, left_motor_speed))
        self.pwm_motor1_backward.ChangeDutyCycle(max(0, -left_motor_speed))
        self.pwm_motor2_forward.ChangeDutyCycle(max(0, right_motor_speed))
        self.pwm_motor2_backward.ChangeDutyCycle(max(0, -right_motor_speed))

        # Determine the direction of each motor based on speed
        # (You might need to adjust this part based on your motor configuration)
        GPIO.output(self.pin_motor1_forward, GPIO.HIGH if left_motor_speed >= 0 else GPIO.LOW)
        GPIO.output(self.pin_motor1_backward, GPIO.LOW if left_motor_speed >= 0 else GPIO.HIGH)
        GPIO.output(self.pin_motor2_forward, GPIO.HIGH if right_motor_speed >= 0 else GPIO.LOW)
        GPIO.output(self.pin_motor2_backward, GPIO.LOW if right_motor_speed >= 0 else GPIO.HIGH)

    def cleanup_gpio(self):
        # Cleanup GPIO before exiting
        self.pwm_motor1_forward.stop()
        self.pwm_motor1_backward.stop()
        self.pwm_motor2_forward.stop()
        self.pwm_motor2_backward.stop()
        GPIO.cleanup()

def main(args=None):
    rclpy.init(args=args)
    node = MotorControlNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.cleanup_gpio()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
