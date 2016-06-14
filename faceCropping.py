import cv2
from os import listdir
from os.path import isfile, join

imagePath = "/root/Images/"
cascPathFace = "/root/haarcascade_frontalface_default.xml"

imageList = listdir(imagePath)

for img in imageList:
	faceCascade = cv2.CascadeClassifier(cascPathFace)

	path  = "/root/Images/"+ str(img)

	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	minisize = (image.shape[1],image.shape[0])
	miniframe = cv2.resize(image, minisize)

	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	#crop padding
	top = 15
	bottom = 15
	right = 15
	left = 15

	for (x, y, w, h) in faces:
		#for face
	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	    cropped_image_1 = image[y:y+h, x:x+w]
	    cropped_image_2 = image[y-top:y+h+bottom, x-left:x+w+right]

	name_for_image1 = "FaceCroppingType1/"+str(img)
	name_for_image2 = "FaceCroppingType2/"+str(img)
	# cv2.imshow("Faces found" ,image)
	cv2.imwrite(name_for_image1, cropped_image_1)
	cv2.imwrite(name_for_image2, cropped_image_2) 

print 'face cropping done..!!'
cv2.waitKey(0)	  
