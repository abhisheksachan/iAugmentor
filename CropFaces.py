import cv2
import os

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Retrieving and Saving Files locations
path_retrieve = "/root/Frames/5mp4"
path_save = "/iAugmentor/CroppedFrames/"

#Reterieving the file list
listing = os.listdir(path_retrieve)

#Go through the list, picking up each image for face detection
for file in listing:
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        #Read the image, turn it into grayscale
        image = cv2.imread(file)
        if image == None:
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #Display original image for comparison
        #cv2.imshow('Original Image', image)
        #cv2.waitKey()

        # Detect image for faces and print the total
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        #print ("Found {0} faces!".format(len(faces)))

        # Crop Padding
        left = 15
        right = 15
        top = 15
        bottom = 15
	#x = 0
	#y = 0
	#w = 0
	#h = 0

        #Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            #print (x, y, w, h)
            img  = image[y-top:y+h+bottom, x-left:x+w+right]
            #cv2.imshow('Cropped Image', img)
            #cv2.waitKey()
            #cv2.destroyAllWindows()

            #Dubugging boxes
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #Final Cropped Image
        cropped_image_1  = image[y-top:y+h+bottom, x-left:x+w+right]
        cropped_image_2 = image[y: y+h, x: x+w]

        #Save the image
        #print ("cropped_{0}_{1}".format(str(x),str(file)))
        cv2.imwrite("FaceCroppingType1/5mp4/"+str(file), cropped_image_1)
        cv2.imwrite("FaceCroppingType1/5mp4/"+str(file), cropped_image_2)

print("DONE")
