#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:35:21 2019

@author: amogh
"""

'''import vlc

media = vlc.MediaPlayer("/home/amogh/Downloads/taxiwala.mkv")
media.play()'''

import webbrowser
import os

new=2
url="isha.sadhguru.org"
browserExe = "chrome"


webbrowser.open(url)
webbrowser.open_new(url)
webbrowser.open_new_tab(url)
print(webbrowser.get())
#os.system("pkill "+browserExe)
