import cv2
from os import listdir
from os.path import isfile, join

imagePath = "/home/abhishek/iAugmentor/Frames/5mp4/frame0.jpg"
cascPathFace = "/home/abhishek/iAugmentor/code/haarcascade_frontalface_default.xml"
cascPathEye = "/home/abhishek/iAugmentor/code/haarcascade_eye.xml"
cascPathMouth = '/home/abhishek/iAugmentor/code/haarcascade_mcs_mouth.xml'
cascPathNose = '/home/abhishek/iAugmentor/code/haarcascade_mcs_nose.xml'

faceCascade = cv2.CascadeClassifier(cascPathFace)
eyeCascade = cv2.CascadeClassifier(cascPathEye)
LefteyeCascade = cv2.CascadeClassifier(cascPathEye)
RighteyeCascade = cv2.CascadeClassifier(cascPathEye)
mouthCascade = cv2.CascadeClassifier(cascPathMouth)
noseCascade = cv2.CascadeClassifier(cascPathNose)

# imageList = listdir(imagePath)

# for img in imageList:

# path  = "/root/Frames/1avi/"+ str(img)
print "1"
image = cv2.imread(imagePath)
if image == None:
	# continue
	cv2.waitKey(1)

print "2"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "faces",faces
print "3"
for (x, y, w, h) in faces:
	print "4"
	#for face
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = image[y:y+h, x:x+w]
	print "roi_gray",roi_gray

    #for eyes
	eyes = eyeCascade.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	nose = noseCascade.detectMultiScale(roi_gray)
	for (np,nq,nr,ns) in nose:
		cv2.rectangle(roi_color,(np,nq),(np+nr,nq+ns), (0,0,0),2)
	
	mouth = mouthCascade.detectMultiScale(roi_gray)
	for (mp,mq,mr,ms) in mouth:
		cv2.rectangle(roi_color,(mp,mq),(mp+mr,mq+ms), (255,255,255),2)	

name = "/home/abhishek/iAugmentor/Frames/results/frame0.jpg"
# cv2.imshow("Faces found" ,image)
cv2.imwrite(name, image)  
print "5"
print 'face detection done..!!'
cv2.waitKey(1)	  
