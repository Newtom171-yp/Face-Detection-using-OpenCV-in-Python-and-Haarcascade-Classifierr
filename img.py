# Importing required libraries
import cv2

# Loading classifier
face_cascade = cv2.CascadeClassifier('PATH of haarcascade_frontalface_default.xml')

# Loading testing image
img = cv2.imread('PATH of Input Image')

# Converting into gray scale image
gray = cv2.imread('Path of Input Image',0)

# Setting parameters
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Setting Rectangular properties
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

# Showing Results
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
