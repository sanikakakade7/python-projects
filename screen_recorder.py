#using opencv we take screenshots every ms and merge them to form a video ##opencv is a python library used for image loading and manipulation
#in numpy we create array to store our screenshots
#screen modulations will be recorded with pywin32
#pyautogui also used for screen recording purpose

import cv2
from win32api import GetSystemMetrics
import pyautogui
import numpy as np
import time #time module will be used to prepare a video in that particular duration

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
#by doing so we capture the entire screen height and width
dim=(width,height)  #the height and width is stored in dim which is needed later

f=cv2.VideoWriter_fourcc(* "XVID")  #XVID is a parent format that contains all the other video formats
#f is a variable to which we pass the format of the video

output=cv2.VideoWriter(r"C:\Users\sanika\PycharmProjects\python small projects\video.mp4v",f,30.0,dim) #after mp4 use v else there is an error
#output is a variable which will store the o/p of video recorded and is stored in file named testvideo.mp4
#after name of file pass the format of video i.e f then how many frames to capture per second normally it is 30 along with dim of video

start_time=time.time()
duration=30
end_time=start_time+duration

while True:
    img=pyautogui.screenshot()   #pyautogui module has screenshot function to take screenshot that is stored in image
    frame=np.array(img)  #the image is then stored in frame that is a numpy array
    final_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #finallly color changes are made in frame and is stored in new frame
    output.write(final_frame)  #the output is a empty box with specified values now we provide i/p to it in form of final_frame
    #which is array of images that have been captured

    curr_time=time.time()
    if curr_time>end_time:
        break


output.release()  #releases the video in given format
print('End of Recording Video Captured')


#we see that duration of video is 6sec i.e 4 sec less than specified duration this occurs due to compilation time