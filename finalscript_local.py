import cv2
import numpy as np

cascPathFace = "/root/haarcascade_frontalface_default.xml"
cascPathEye = "/root/code/haarcascade_eye.xml"

faceCascade = cv2.CascadeClassifier(cascPathFace)
eyeCascade = cv2.CascadeClassifier(cascPathEye)

top = 15
bottom = 15
right = 15
left = 15

cap = cv2.VideoCapture("1.mp4")
count = 0

ret, frame = cap.read()

while ret:

	ret,  frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	for (x, y, w, h) in faces:
		#for face
	    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	    roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #for eyes
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cropped_image_1 = frame[y:y+h, x:x+w]
	cropped_image_2 = frame[y-top:y+h+bottom, x-left:x+w+right]

	name_for_image1 = "FaceCroppingType1/1mp4/"+"frame%d.jpg"%count
	name_for_image2 = "FaceCroppingType2/1mp4/"+"frame%d.jpg"%count

	# cv2.imshow("Faces found" ,image)
	cv2.imwrite(name_for_image1, cropped_image_1)
	cv2.imwrite(name_for_image2, cropped_image_2)
	count +=1
	
print 'final script done..!!'
cv2.waitKey(0)


 