import numpy 
import cv2 
import datetime 
  
# open the video 
cap = cv2.VideoCapture(0) 
 
while True: 
    ret, frame = cap.read() 
  
        # font you want to display 
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
  
        # Get date and time and save it in a variable 
    text1= "Chaitanya's Cam" 
    dt = str(datetime.datetime.now()) 
    frame1=cv2.flip(frame,1)  
  
        # put the dt variable over the video frame
    frame1 = cv2.putText(frame1, dt, 
                        (10, 450), 
                        font, 1, 
                        (210, 155, 155),  
                        4, cv2.LINE_8) 
        # show the video 
  
    cv2.imshow('frame', frame1) 
  
    k = cv2.waitKey(5)
    if k == 27: 
        break
        # define the key to close the window       
          
# release the vid object 
cap.release()   
# close all the opened windows. 
cv2.destroyAllWindows()