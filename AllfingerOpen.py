from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#Take the input from the user and perform all fingers close and open
servo=int(input('Enter user input>>>  '))
if servo== 1:
    print(servo)
    while True:
        sleep(1)
        kit.servo[0].angle = 180
        kit.servo[1].angle = 180
        kit.servo[2].angle = 180
        kit.servo[3].angle = 180
        kit.servo[4].angle = 180
        sleep(1)
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
        kit.servo[2].angle = 0
        kit.servo[3].angle = 0
        kit.servo[4].angle = 0

        break
          
else:
    print('Enter the correct number')