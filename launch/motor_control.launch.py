# my_motor_control_node.py
import RPi.GPIO as GPIO
from std_msgs.msg import String
from rclpy.node import Node

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        GPIO.setmode(GPIO.BOARD)

        # Set up GPIO pins for motor control
        self.left_forward = 12  # Replace with the actual GPIO pin
        self.left_backward = 32  # Replace with the actual GPIO pin
        self.right_forward = 33  # Replace with the actual GPIO pin
        self.right_backward = 35  # Replace with the actual GPIO pin
        GPIO.setup(self.left_forward, GPIO.OUT)
        GPIO.setup(self.left_backward, GPIO.OUT)
        GPIO.setup(self.right_forward, GPIO.OUT)
        GPIO.setup(self.right_forward, GPIO.OUT)

        left_forward_pwm = GPIO.PWM(self.left_forward, 90)
        left_backward_pwm = GPIO.PWM(self.left_backward, 90)
        right_forward_pwm = GPIO.PWM(self.right_forward, 90)
        right_backward_pwm = GPIO.PWM(self.right_backward, 90)

        # Create a subscriber to receive motor control commands
        self.subscription = self.create_subscription(
            String,
            'motor_control',
            self.control_callback,
            10
        )
        self.subscription

    def control_callback(self, msg):
        cmd = msg.data
        if cmd == 'forward':
            GPIO.output(self.pin_motor1, GPIO.HIGH)
            GPIO.output(self.pin_motor2, GPIO.LOW)
        elif cmd == 'backward':
            GPIO.output(self.pin_motor1, GPIO.LOW)
            GPIO.output(self.pin_motor2, GPIO.HIGH)
        elif cmd == 'stop':
            GPIO.output(self.pin_motor1, GPIO.LOW)
            GPIO.output(self.pin_motor2, GPIO.LOW)

def main(args=None):
    rclpy.init(args=args)
    node = MotorControlNode()
    rclpy.spin(node)
    GPIO.cleanup()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
