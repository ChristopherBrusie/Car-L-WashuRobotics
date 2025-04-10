import time
from adafruit_servokit import ServoKit
import keyboard  

kit = ServoKit(channels=16)

try:
	while True:
		if keyboard.is_pressed('w'):
			kit.continuous_servo[0].throttle = -1
			kit.continuous_servo[1].throttle = 1
			kit.continuous_servo[2].throttle = 1
			kit.continuous_servo[3].throttle = -1
		elif keyboard.is_pressed('s'):
			kit.continuous_servo[0].throttle = 1
			kit.continuous_servo[1].throttle = -1
			kit.continuous_servo[2].throttle = -1
			kit.continuous_servo[3].throttle = 1	
		elif keyboard.is_pressed('a'):
			kit.continuous_servo[0].throttle = -1
			kit.continuous_servo[1].throttle = -1
			kit.continuous_servo[2].throttle = -1
			kit.continuous_servo[3].throttle = -1
		elif keyboard.is_pressed('d'):
			kit.continuous_servo[0].throttle = 1
			kit.continuous_servo[1].throttle = 1
			kit.continuous_servo[2].throttle = 1
			kit.continuous_servo[3].throttle = 1
		else:
			kit.continuous_servo[0].throttle = 0
			kit.continuous_servo[1].throttle = 0
			kit.continuous_servo[2].throttle = 0
			kit.continuous_servo[3].throttle = 0
except KeyboardInterrupt:
	print("stopped")
finally:
	kit.continuous_servo[0].throttle = 0
	kit.continuous_servo[1].throttle = 0
	kit.continuous_servo[2].throttle = 0
	kit.continuous_servo[3].throttle = 0
	print("servos stopped")
