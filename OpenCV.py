import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import *

#All fingers close
kit.servo[0].angle = 180
kit.servo[1].angle = 180
kit.servo[2].angle = 180
kit.servo[3].angle = 180
kit.servo[4].angle = 180


# 0 = Thumb
# 1 = Index
# 2 = Middle
# 3 = Ring
# 4 = Pinky


cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]

#To detect the specific finger is open or close and gives the command to servo
while True:

     ret, frame = cap.read()
     frame1 = cv2.resize(frame, (640, 480))

     
     a=findpostion(frame1)
     b=findnameoflandmark(frame1)
     
      
 
     if len(b and a)!=0:
        finger=[]
        if a[2][1:] < a[4][1:]: 
           finger.append(1)
           print (b[4])
           kit.servo[0].angle = 0

        if a[6][2:] < a[8][2:]: 
           finger.append(1)
           print (b[8])
           kit.servo[1].angle = 180

        if a[10][2:] < a[12][2:]: 
           finger.append(1)
           print (b[12])
           kit.servo[2].angle = 180

        if a[14][2:] < a[16][2:]: 
           finger.append(1)
           print (b[16])
           kit.servo[3].angle = 180

        if a[18][2:] < a[20][2:]: 
           finger.append(1)
           print (b[20])
           kit.servo[4].angle = 180

           
        if a[6][2:] > a[8][2:]: 
               kit.servo[1].angle=0 
        if a[10][2:] > a[12][2:]: 
               kit.servo[2].angle=0
        if a[14][2:] > a[16][2:]: 
               kit.servo[3].angle=0
        if a[18][2:] > a[20][2:]: 
               kit.servo[4].angle=0
        if a[3][1:] > a[4][1:]: 
               kit.servo[0].angle= 180
                       
        else:
           finger.append(0)   

           
     
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"):
        speak("sir you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
                    
     if key == ord("s"):
       break