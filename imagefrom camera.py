import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(1)
_,img = cam.read()#To read frame from the camera
cv2.imwrite("imagefromCamera.jpg",img)
cam.release()#This will enable us to use it in another application
