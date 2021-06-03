import cv2
import mouse
import pyautogui,time
pyautogui.FAILSAFE = True

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
rec=cv2.face.LBPHFaceRecognizer_create() 
cap = cv2.VideoCapture(0)
rec.read("trainingData.yml")
  
# loop runs if capturing has been initialized. 
while (True):  
  
    # reads frames from a camera 
    ret, img = cap.read()  
  
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("No of faces found:",len(faces))
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        print(id)
        if(id==1):
            id="Chaitanya"
        elif(id==2):
            id="Not Recognized"
        cv2.putText(img, str(id), (x,y+h), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (0, 0, 255))        
      
    # Display an image in a window 
    cv2.imshow('img',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(5)
    if k == 27: 
        break
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  
