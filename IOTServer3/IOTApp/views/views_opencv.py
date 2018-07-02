from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np

@csrf_exempt
def opencv(request):
    mpfilename = './IOTApp/static/images/' + "fire" + '.mp4' 
    
    wfilename1 = './IOTApp/static/images/' + "fire1" + '.jpg'
    wfilename2 = './IOTApp/static/images/' + "fire2" + '.jpg'
    wfilename3 = './IOTApp/static/images/' + "fire3" + '.jpg'
    wfilename4 = './IOTApp/static/images/' + "fire4" + '.jpg'

    rfilename1 = '/static/images/' + "fire1" + '.jpg'
    rfilename2 = '/static/images/' + "fire2" + '.jpg'
    rfilename3 = '/static/images/' + "fire3" + '.jpg'
    rfilename4 = '/static/images/' + "fire4" + '.jpg'

    video = cv2.VideoCapture(mpfilename)    
    grabbed, frame = video.read()

    blur = cv2.GaussianBlur(frame,(21,21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower = [18,50,50]
    upper = [35,255,255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, hsv, mask=mask)

    #img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(wfilename1, frame)
    cv2.imwrite(wfilename2, blur)
    cv2.imwrite(wfilename3, hsv)
    cv2.imwrite(wfilename4, output)        

    video.release()
    return render(request,'IOTApp/opencv.html',{'filename1':rfilename1,'filename2':rfilename2,'filename3':rfilename3,'filename4':rfilename4})

