#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:37:41 2019

@author: amogh
"""

import cv2
import numpy as np
import webbrowser
import os
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

from keras.models import load_model
import time

cap = cv2.VideoCapture(0)
x=50
y=50
w=200
h=200
countw=0
countt=0

def predict():
    img_path = 'webcam.jpeg'
    img = image.load_img(img_path, target_size=(64, 64))
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return (np.argmax(new_model.predict(x)))

def open_browser(url):
    if(countw<3):
        webbrowser.open(url)
        countw+=1
def open_newtab(url):
    if (countt<3):
        webbrowser.open_new_tab(url)
        countt+=1
        
def open_newwindow(url):
    if(countw<3):
        webbrowser.open_new(url)
        countw+=1
    
def close_browser():
    os.system("pkill "+browserExe)


new_model = load_model('hand_model.h5')   
new=2
url="isha.sadhguru.org"
browserExe = "chrome" 
while(True):
    
    
    ret,frame = cap.read()
    
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imwrite('webcam.jpeg',frame[y:(y+h), x:(x+w)])
    digit = predict()
    print(digit)
    cv2.putText(frame, str(digit), (330, 50),
    					cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
    '''
    cv2.putText(frame, '1.Everything Working', (0, 330),
    					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '2.Open Browser', (0, 350),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '3.Open New Window', (0, 370),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '4.Open New Tab', (0, 390),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '5.Close Browser', (0, 410),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)'''
    cv2.imshow("Frame",frame)
    
    
    
    #print(digit)
    
    
    if(cv2.waitKey(1)==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
