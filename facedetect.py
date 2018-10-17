import numpy
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('leo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h)in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
    
cv2.imshow('output',img) 
      
cv2.waitKey(5000) 

cv2.destroyAllWindows() 
