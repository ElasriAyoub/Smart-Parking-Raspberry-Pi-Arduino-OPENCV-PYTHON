#CRER Project - SMART PARKING

import cv2
import csv
from pygame import mixer
from playsound import playsound
import time

#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT)

class spots:
    loc1 = 0
    loc2 = 0

def drawRectangle1(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    # counting the white pixels
    pix = cv2.countNonZero(edges)
    # testing if the pixels number is in the given range
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        spots.loc1 += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)

def drawRectangle2(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    # counting the white pixels
    pix = cv2.countNonZero(edges)
    # testing if the pixels number is in the given range
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (255, 0, 0), 3)
        spots.loc2 += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 225, 255), 3)


def callback(foo):
    pass


with open('data/rois.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)


# converting the values to integer
rois = [[int(float(j)) for j in i] for i in rois]


cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1', 'parameters', 186, 700, callback)
cv2.createTrackbar('Threshold2', 'parameters', 122, 700, callback)
cv2.createTrackbar('Min pixels', 'parameters', 0, 1500, callback)
cv2.createTrackbar('Max pixels', 'parameters', 323, 1500, callback)


cap = cv2.VideoCapture(1)
k = 0
cpt = 0
while True:
    spots.loc1 = 0
    spots.loc2 = 0
    ret, frame = cap.read()
    ret2, frame2 = cap.read()
    min = cv2.getTrackbarPos('Min pixels', 'parameters')
    max = cv2.getTrackbarPos('Max pixels', 'parameters')
    lowThreshold = cv2.getTrackbarPos('Threshold1', 'parameters')
    highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')


    for i in range(len(rois)):
        drawRectangle1(frame, rois[i][0], rois[i][1], rois[i][2], rois[i][3])
        k = k + 1
        if(k==(len(rois)-1)):
            break
    drawRectangle2(frame, rois[k][0], rois[k][1], rois[k][2], rois[k][3])
    k = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Available spots: ' + str(spots.loc1), (10, 30), font, 1, (0, 255, 0), 3)
    cv2.imshow('frame', frame)

    canny = cv2.Canny(frame2, lowThreshold, highThreshold)
    cv2.imshow('canny', canny)
    if(spots.loc1==0 and spots.loc2==0):

        if(cpt==40):
            playsound('vocal/full/full1.mp3')
            cpt = 0
        cpt = cpt + 1
    if(spots.loc1>0 and spots.loc2==0):
        if (cpt == 40):
 #           GPIO.output(18, GPIO.HIGH)
            playsound('vocal/welcome/welcome1.mp3')
            cpt = 0
            time.sleep(1)
  #          GPIO.output(18, GPIO.LOW)

        cpt = cpt + 1

    #print(spots.loc2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
