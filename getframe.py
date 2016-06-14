import cv2
import numpy as np

cap = cv2.VideoCapture("1.mp4")
count = 0
ret, frame = cap.read()

while ret:
	ret,  frame = cap.read()

	name = "Images/frame%d.jpg"%count
	cv2.imwrite(name, frame)
	count +=1


