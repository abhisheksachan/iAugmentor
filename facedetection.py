import cv2
from os import listdir
from os.path import isfile, join

imagePath = "/root/Frames/1avi"
cascPathFace = "/root/haarcascade_frontalface_default.xml"
cascPathEye = "/root/haarcascade_eye.xml"

faceCascade = cv2.CascadeClassifier(cascPathFace)
eyeCascade = cv2.CascadeClassifier(cascPathEye)

imageList = listdir(imagePath)

for img in imageList:

	path  = "/root/Frames/1avi/"+ str(img)

	image = cv2.imread(path)
	if image == None:
		continue

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	for (x, y, w, h) in faces:
		#for face
	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	    roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        #for eyes
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	name = "FaceDetection/1avi/"+str(img)
	# cv2.imshow("Faces found" ,image)
	cv2.imwrite(name, image)  

print 'face detection done..!!'
cv2.waitKey(0)	  
