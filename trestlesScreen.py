__author__ = 'stephencrook'
#script opens webbrowser, navigates to the trestles streaming cam, and takes 4 pics, 8 sec apart from each other"

import webbrowser
import pyscreenshot
import time
import os

#open surf cam
#change from google to proper cam when ready
#http://www.surfline.com/surf-report/lower-trestles-southern-california_4740/
webbrowser.open("http://www.google.com")

#creates folder to put screenshots in
monthDayHour = time.strftime("%m-%d-%Y-%H")
newDir = r'/Users/stephencrook/Documents/Work/Code/surfPredict/screenShot/' + monthDayHour + "00"
os.makedirs(newDir)
os.chdir(newDir)

for i in range(0, 4):

    #wait 8 sec before taking another photo
    time.sleep(10)

    currentTime = time.strftime("%m-%d-%Y-%H-%M-%S")

    #screenshot
    pyscreenshot.grab_to_file('trestles-' + currentTime + '.png')