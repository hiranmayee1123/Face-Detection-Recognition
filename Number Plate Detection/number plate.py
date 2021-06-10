import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.jpg',cv2.IMREAD_COLOR)
img = imutils.resize(img, width=500 )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1=img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)
cv2.imshow("img1",img1)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
screenCnt = None #will store the number plate contour
img2 = img.copy()
cv2.drawContours(img2,cnts,-1,(0,255,0),3) 
cv2.imshow("img2",img2) #top 30 contours

count=0
idx=7
# loop over contours
for c in cnts:
  # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4: #chooses contours with 4 corners
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c) #finds co-ordinates of the plate
                new_img=img[y:y+h,x:x+w]
                cv2.imwrite('./'+str(idx)+'.png',new_img) #stores the new image
                idx+=1
                break
            #draws the selected contour on original image        
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Final image with plate detected",img)

Cropped_loc='./7.png' #the filename of cropped image
cv2.imshow("cropped",cv2.imread(Cropped_loc))
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #exe file for using ocr 

text=pytesseract.image_to_string(Cropped_loc,lang='eng') #converts image characters to string
print("Number is:" ,text)
cv2.waitKey(0)
cv2.destroyAllWindows() 
