# import the necessary packages
import cv2
import os
import sys
import random 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = True
click_count = 0
image_count = 0
left_left_eye = (0,0)
right_left_eye = (0,0)
left_right_eye = (0,0)
right_right_eye = (0,0)
nose = (0,0)
left_mouth = (0,0)
right_mouth = (0,0)
total_images = 50


def click_and_save(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping, click_count, left_left_eye,left_right_eye,right_left_eye,right_right_eye,left_mouth,right_mouth,nose

	if event == cv2.EVENT_LBUTTONDOWN:
		print x,y
		click_count += 1
		
		if click_count == 1:
			left_left_eye = (left_left_eye[0]+x, left_left_eye[1]+y)
		
		if click_count == 2:
			right_left_eye = (right_left_eye[0]+x, right_left_eye[1]+y)
		
		if click_count == 3:
			left_right_eye = (left_right_eye[0]+x, left_right_eye[1]+y)
		
		if click_count == 4:
			right_right_eye = (right_right_eye[0]+x, right_right_eye[1]+y)
		
		if click_count == 5:
			nose = (nose[0]+x, nose[1]+y)
		
		if click_count == 6:
			left_mouth = (left_mouth[0]+x, left_mouth[1]+y)
		
		if click_count == 7:
			right_mouth = (right_mouth[0]+x, right_mouth[1]+y)

		refPt.append((x, y))

		cv2.rectangle(image, (x,y), (x,y), (0, 255, 0), 2)
		cv2.imshow("image", image)

lfw_path = "/home/abhishek/iAugmentor/lfw2"
lfw_folders = os.listdir(lfw_path)
random.shuffle(lfw_folders)

fo = open("facialpoints.txt", "wb")
for folder in lfw_folders:
	print folder
	images = os.listdir(lfw_path + "/" + str(folder))

	for img in images:

		print img
		image = cv2.imread(lfw_path + "/" + str(folder) + "/" + str(img))

		cv2.namedWindow("image")
		cv2.setMouseCallback("image", click_and_save)
		 
		# keep looping until the 'q' key is pressed
		while cropping:
			# display the image and wait for a keypress
			cv2.imshow("image", image)
			key = cv2.waitKey(1) & 0xFF
		 	
		 	if click_count == 7:
		 		break
			# if the 'r' key is pressed, reset the cropping region
			if key == ord("r"):
				click_count = 0
				image = clone.copy()
		 
			# if the 'c' key is pressed, break from the loop
			elif key == ord("c"):
				break

		print refPt
		fo.write('\n'+"name: "+ str(img) +"  points:  "+str(refPt))	
		click_count = 0	
		refPt = []
		cv2.destroyAllWindows()

		#increasing image count		
		image_count += 1	 
		# if there are two reference points, then crop the region of interest
		# from teh image and display it
		if image_count == total_images:
			print left_left_eye[0]/total_images,left_left_eye[1]/total_images 
			print right_left_eye[0]/total_images, right_left_eye[1]/total_images
			print left_right_eye[0]/total_images, left_right_eye[1]/total_images
			print right_right_eye[0]/total_images, right_right_eye[1]/total_images
			print nose[0]/total_images, nose[1]/total_images
			print left_mouth[0]/total_images, left_mouth[1]/total_images
			print right_mouth[0]/total_images, right_mouth[1]/total_images
			sys.exit()
		
		break
		# fo.write('\n \n \n' + "Final points are")
		# fo.write('\n'+"left eye:   "+ str(left_left_eye) + "  "+ str(right_left_eye))
		# fo.write('\n'+"right eye:   "+ str(left_right_eye) + "  "+ str(right_right_eye))
		# fo.write('\n'+"nose:   "+ str(nose))
		# fo.write('\n'+"mouth:   "+ str(left_mouth) + "  "+ str(right_mouth))
		# close all open windows
		
