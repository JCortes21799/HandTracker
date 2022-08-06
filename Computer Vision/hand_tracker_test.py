import mediapipe as mp #Mediapipe for palm models
import numpy as np     #Mathetical math operations
import cv2             #OpenCV for computer vision
import time
import math
#Testing grounds for hand tracking
#Log: 8/5/22: Beginning of project

#Firt thing we will do is simple Hand tracking using libraries
IM_HEIGHT = 480
IM_WIDTH = 480

#Resize camera window
def resize_and_show(image):
    height, width = image.shape[:2] #Get the image parameters
    if (height < width):
        img = cv2.resize(image, IM_WIDTH, math.floor(height/(width/IM_WIDTH)))
    else:
        img = cv2.resize(image, math.floor(width/(height/IM_HEIGHT)), IM_HEIGHT)
    cv2.imshow(img)

    return

#Here we will be using the mediapipe processing pipeline to draw the digits
mp_hands = mp.solutions.hands #This is there hand model
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cam = cv2.VideoCapture(1) #Using the first accesible
while True:
    #Running modified mp processing example
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        success, image = cv2.VideoCapture(1)
        #Flipping + changing color of image
        results = hands.process(cv2.flip(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 1))
        
        print("Handness:")
        print(results.multi_handedness)
