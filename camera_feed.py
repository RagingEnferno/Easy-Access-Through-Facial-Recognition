from cv2 import *
import sys
import os
import time

#start = time.time()

def camera_feed():
    absFilePath = os.path.abspath(__file__)
    #print(absFilePath)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    #print(fileDir)
    parentDir = os.path.dirname(fileDir)
    #print(parentDir)


    cameraFeedCounter = 0;
    while os.path.isfile(f"{parentDir}/images/camera_feed{cameraFeedCounter}.jpg"):
         cameraFeedCounter += 1


    #end = time.time()
    #print(end - start)

    # initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    time.sleep(.7)
    s, img = cam.read()
    if s:    # frame captured without any errors
         #namedWindow("camera-feed-test",cv2.WINDOW_AUTOSIZE)
        #imshow("camera-feed-test",img)
        #waitKey(1000)
        #destroyWindow("camera-feed-test")
        imwrite(f"{parentDir}/images/camera_feed{cameraFeedCounter}.jpg",img) #save image
    else:
        print("There was an error capturing image data from the camera.")

    #end = time.time()
    #print(end - start)
    return f"{parentDir}/images/camera_feed{cameraFeedCounter}.jpg"