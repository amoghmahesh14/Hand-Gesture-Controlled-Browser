#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:19:46 2019

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

def predict():
    img_path = 'webcam.jpeg'
    img = image.load_img(img_path, target_size=(64, 64))
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return (np.argmax(new_model.predict(x)))

def open_browser(url,countw):
    if(countw<1):
        webbrowser.open(url)
        countw+=1
def open_newtab(url,countt):
    if (countt<1):
        webbrowser.open_new_tab(url)
        countt+=1
        
def open_newwindow(url):
    if(countw<3):
        webbrowser.open_new(url)
        countw+=1
    
def close_browser(countw,countt):
    os.system("pkill "+browserExe)
    countt=0
    countw=0

countw=0
countt=0

new_model = load_model('hand_model.h5')   
new=2
url="www.google.com"
browserExe = "chrome" 
i=0

while(True):
    
    
    ret,frame = cap.read()
    
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imwrite('webcam.jpeg',frame[y:(y+h), x:(x+w)])
    digit = predict()
    print(digit)
    if(digit==0 or digit==1):
            cv2.putText(frame, "SYSYTEM IS WORKING", (330, 80),
            					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    if(i%100==0):
        
        
        if(digit==2 or digit==3):
            cv2.putText(frame, "BROWSER CLOSED", (330, 80),
            					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
            close_browser(countw,countt)
        if(digit==4):
            open_browser(url,countw)
        if(digit==5):
            open_newtab(url,countt)
            
    cv2.putText(frame, str(digit), (330, 50),
    					cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
    cv2.putText(frame, '0 AND 1-System Check', (50, 330),
    					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '2 AND 3-Close Browser', (50, 350),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '4-Open Browser', (50, 370),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    cv2.putText(frame, '5-Open New Tab', (50, 390),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255), 1)
    
    cv2.imshow("Frame",frame)
    
 
    i+=1
    if(cv2.waitKey(1)==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
