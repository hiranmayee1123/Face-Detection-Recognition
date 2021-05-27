import cv2 
import time 
  
# SET THE COUNTDOWN TIMER 

TIMER = int(5) 
   
# Open the camera 
cap = cv2.VideoCapture(0)  
  
while True: 
      
    # Read and display each frame 
    ret, img = cap.read()
    img1=cv2.flip(img,1) 
    cv2.imshow('a', img1) 
  
    # check for the key pressed 
    k = cv2.waitKey(125)
       
    # set the key for the countdown 
    # to begin. Here we set c 
    if k == ord('c'): 
        prev = time.time() 
  
        while TIMER >= 0: 
            ret, img = cap.read()
            img1=cv2.flip(img,1) 
  
            # Display countdown on each frame 
            # specify the font and draw the 
            # countdown using puttext 
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(img1, str(TIMER),  
                        (200, 250), font, 
                        7, (0, 255, 255), 
                        4, cv2.LINE_AA) 
            cv2.imshow('a', img1) 
            cv2.waitKey(125) 
  
            # current time 
            cur = time.time() 
  
            # Update and keep track of Countdown 
            # if time elapsed is one second  
            # than decrese the counter 
            if cur-prev >= 1: 
                prev = cur 
                TIMER = TIMER-1
  
        else: 
            ret, img = cap.read()
            img1=cv2.flip(img,1) 
  
            # Display the clicked frame for 2  
            # sec.You can increase time in  
            # waitKey also 
            cv2.imshow('a', img1) 
  
            # time for which image displayed 
            cv2.waitKey(2000) 
  
            # Save the frame 
            cv2.imwrite('camera.jpg', img1) 
            
            # HERE we can reset the Countdown timer 
            # if we want more Capture without closing 
            # the camera 
  
    # Press Esc to exit 
    elif k == 27: 
        break
  
# close the camera 
cap.release() 
   
# close all the opened windows 
cv2.destroyAllWindows()