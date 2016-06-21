import cv2
import os

#Cascade Files
cascadeFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascadeEye = cv2.CascadeClassifier("haarcascade_eye.xml")
cascadeNose = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
cascadeMouth = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")

#Save path
#path_retrieve = "S:/Users/Sahil Verma/PycharmProjects/iAugmentor/"
path_retrieve = "/home/abhishek/iAugmentor/lfw2"
path_save = "/home/abhishek/FacialDetection/"
text_name = "test.txt"

#Values required
nx = 0
ny = 0
nw = 0
nh = 0
thickness = 3

#Retrieve the file list
listing1 = os.listdir(path_retrieve)
print (list(listing1))

with open("test.txt", "w") as myfile:
    myfile.write("Facial Points")

#Go through the list, picking up each image for facial detection
for file1 in listing1:
    listing2 = os.listdir(path_retrieve +"/"+ file1)

    for file2 in listing2:
        if file2.lower().endswith(('.png', '.jpg', '.jpeg')):

            # Reading and displaying image
            image = cv2.imread(path_retrieve +"/" + file1 + "/"+ file2)
            cv2.imshow("Original", image)
            cv2.waitKey()

            with open(text_name, "a") as myfile:
                myfile.write("\nIMAGE: " + str(file2))
            print("IMAGE: " + str(file2))

            # Converting to gray, for reduction of noise
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            #FACES
            #Reading the faces in each image and going through all of them
            faces = cascadeFace.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = image[y:y + h, x:x + w]


                #EYES
                #Reading the eyes in each image and going through all of them
                eyes = cascadeEye.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    #Co-ordinates for all eye points
                    left_side_of_eye_x = ex + int(ew/10)
                    left_side_of_eye_y = ey + int(eh/2)
                    right_side_of_eye_x = ex + int(0.9 * ew)
                    right_side_of_eye_y = ey + int(eh/2)

                    #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
                    cv2.line(roi_color, (left_side_of_eye_x, left_side_of_eye_y),
                             (left_side_of_eye_x + 1, left_side_of_eye_y), (0, 0, 255), thickness)
                    cv2.line(roi_color, (right_side_of_eye_x, right_side_of_eye_y),
                             (right_side_of_eye_x + 1, right_side_of_eye_y), (0, 0, 255), thickness)

                    with open(text_name, "a") as myfile:
                        myfile.write(" LSE: (" + str(left_side_of_eye_x) + "," + str(left_side_of_eye_y) + ") ")
                        myfile.write(" RSE: (" + str(right_side_of_eye_x) + "," + str(right_side_of_eye_y) + ") ")

                    print("LSE: (" + str(left_side_of_eye_x) + "," + str(left_side_of_eye_y) + ") ")
                    print("RSE: (" + str(right_side_of_eye_x) + "," + str(right_side_of_eye_y) + ") ")


                #NOSE
                #Reading the nose ONCE in each image
                nose = cascadeNose.detectMultiScale(roi_gray)
                for (nx, ny, nw, nh) in nose:
                    #Co-ordinates for nose tip
                    nose_tip_x = nx + int(nw/2)
                    nose_tip_y = ny + int(nh/2)

                    #cv2.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (0, 255, 0), 2)
                    cv2.line(roi_color, (nose_tip_x, nose_tip_y),
                             (nose_tip_x + 1, nose_tip_y + 1), (0, 255, 0), thickness)

                    with open(text_name, "a") as myfile:
                        myfile.write("Nose: (" + str(nose_tip_x) + "," + str(nose_tip_y) + ") ")

                    print("Nose: (" + str(nose_tip_x) + "," + str(nose_tip_y) + ") ")

                    break


                #LIPS
                #Reading the lips in each image and going through all of them
                mouth = cascadeMouth.detectMultiScale(roi_gray)
                for (mx, my, mw, mh) in mouth:
                    # Co-ordinates for lip ends
                    left_side_of_lips_x = mx + int(mw/10)
                    left_side_of_lips_y = my + int(0.3*mh)
                    right_side_of_lips_x = mx + int(0.9*mw)
                    right_side_of_lips_y = my + int(0.3*mh)

                    #Mouth must be below nose (obviously)
                    if (ny + int(0.6*nh) < my):
                        #cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 0, 0), 2)
                        cv2.line(roi_color, (left_side_of_lips_x, left_side_of_lips_y),
                                 (left_side_of_lips_x + 1, left_side_of_lips_y), (255, 0, 0), thickness)
                        cv2.line(roi_color, (right_side_of_lips_x, right_side_of_lips_y),
                                 (right_side_of_lips_x + 1, right_side_of_lips_y),(255, 0, 0), thickness)

                    with open(text_name, "a") as myfile:
                        myfile.write(" LSL: (" + str(left_side_of_lips_x) + "," + str(left_side_of_lips_y) + ") ")
                        myfile.write(" RSL: (" + str(right_side_of_lips_x) + "," + str(right_side_of_lips_y) + ") ")

                    print("LSL: (" + str(left_side_of_lips_x) + "," + str(left_side_of_lips_y) + ") ")
                    print("RSL: (" + str(right_side_of_lips_x) + "," + str(right_side_of_lips_y) + ") ")

                    break

            #Displaying final output
            cv2.imshow("Image", image)
            cv2.imwrite(path_save + "/" + "{0}".format(str(file2)), image)
            cv2.waitKey()
            cv2.destroyAllWindows()

print ("DONE")