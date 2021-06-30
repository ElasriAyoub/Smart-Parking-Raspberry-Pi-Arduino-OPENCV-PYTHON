#CRER Project - SMART PARKING

import cv2
import csv

cap = cv2.VideoCapture(0)
suc, image = cap.read()

cv2.imwrite("frame0.jpg", image)
img = cv2.imread("frame0.jpg")

r = cv2.selectROIs('ROI Selector', img, showCrosshair=False, fromCenter=False)

rlist = r.tolist()
print(rlist)

with open('data/rois.csv', 'w', newline='') as outf:
  csvw = csv.writer(outf)
  csvw.writerows(rlist)

cap.release()
cv2.destroyAllWindows()
