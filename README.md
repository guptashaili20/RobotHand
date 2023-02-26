# Robot Hand ![OK robot hand Stock Photo](https://user-images.githubusercontent.com/100229177/221417584-fccd6dab-c520-46e9-8048-14444e87c0a5.png)

## A robot hand that mimic human hand gesture using OpenCV which is installed in Raspberry pi 4B.
## General Information-
This project is a prototype showcasing the industrial application of OpenCV associated with Universal Robot(UR5e).
- Components used - Raspberry Pi(4B), Webcam(Any webcame more than 5 MP), Servomotor(MG 995)
## Raspbery pi Installation - 
We need OS buster to do the project. Installation [Link](https://core-electronics.com.au/guides/raspberry-pi/flash-buster-os-pi/)
- Step 1 -- Download the zip file(in Raspberry Pi 4B)
- Step 2 -- You will see following folder in the zip file - (a)All fingersopen.py  (b) Module.py  (c) OpenCV.py  (d)Readme.md
## Install Packages in Raspberry pi -- 
1. To install Opencv in raspberry pi 4B follow this command on terminal -
 - sudo apt-get update && sudo apt-get upgrade
 - sudo nano /etc/dphys-swapfile
 - Now swape the swapesize to CONF_SWAPSIZE = 100 to CONF_SWAPSIZE=2048
 - Having done this press Ctrl-X, Y, and then Enter Key to save these changes.
 - sudo apt-get install build-essential cmake pkg-config
- sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
- sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
- sudo apt-get install libxvidcore-dev libx264-dev
- sudo apt-get install libgtk2.0-dev libgtk-3-dev
- sudo apt-get install libatlas-base-dev gfortran
- sudo pip3 install numpy
- wget -O opencv.zip https://github.com/opencv/opencv/archive/4.4.0.zip
- wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.4.0.zip
- unzip opencv.zip
- unzip opencv_contrib.zip
- cd ~/opencv-4.4.0/
- mkdir build
- cd build
- cmake -D CMAKE_BUILD_TYPE=RELEASE \
                                -D CMAKE_INSTALL_PREFIX=/usr/local \
                                -D INSTALL_PYTHON_EXAMPLES=ON \
                                -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-4.4.0/modules \
                                -D BUILD_EXAMPLES=ON ..
- make -j $(nproc)
- Above Command will take over an hour to install and there will be no indication of how much longer it will take.
- sudo make install && sudo ldconfig
- sudo reboot

2. To install Mediapipe in Raspberry Pi 4B(For reference) [Mediapipelink](https://pypi.org/project/mediapipe-rpi4/)
- sudo pip3 install mediapipe-rpi4

3. To install motor driver package(PCA9685 module)
- To use PCA9685 we have to install this library adafruit_servokit.h
- Command - sudo pip3 install adafruit-circuitpython-servokit

4. To install gtts 
- sudo pip3 install gTTS

# Programming using Thonny Python IDE-

# module.py
Importing necessary libraries needed for the code - 
<pre>
import cv2
import mediapipe as freedomtech
from gtts import gTTS
import os
</pre> 

Function for Text to speech conversion - 
<pre>
def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
</pre>

To find position of the hand in a frame - 
<pre>
def findpostion(frame1):
    list=[]
    results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
       for handLandmarks in results.multi_hand_landmarks:
           drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
           list=[]
           for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * w)
                y = int(pt.y * h)
                list.append([id,x,y])

    return list
</pre>

Finding Landmark of the fingers - 
<pre>
def findnameoflandmark(frame1):
     list=[]
     results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
     if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:


            for point in handsModule.HandLandmark:
                 list.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
     return list
</pre>
 
# Open.py - 
This code is the main file, where we are using OpenCV platform to track and detect the human hand motion using mediapipe model.

Importing necessary Libraries.
<pre>
import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import *
 </pre> 
 
 Assignment of Fingers to servomotor -
<pre>
 0 = Thumb
 1 = Index
 2 = Middle
 3 = Ring
 4 = Pinky
</pre>
                   
In Real time Human Hand detection using this, and deciding the window frame and size -                    
 <pre>cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]

#To detect the specific finger is open or close and gives the command to servo
while True:

     ret, frame = cap.read()
     frame1 = cv2.resize(frame, (640, 480))</pre>

To detect which finger is up or down by using their Landmark position w.r.t. knuckle Landmark -     
<pre>
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
     key = cv2.waitKey(1) & 0xFF</pre>
                 
To convert the text into speech mode.                   
<pre> if key == ord("q"):
        speak("sir you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
                    
     if key == ord("s"):
       break</pre>
                   
# Summary 
This 3D printable hand, which results in a safe interaction with human bodies. Each gripper finger is designed to mimic the real-world movement of a human finger.
Thats how it is installed on to a Universal Robot(UR5e) to act as a gripper. 
