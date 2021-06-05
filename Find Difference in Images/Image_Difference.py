from skimage.measure import compare_ssim
import imutils
import cv2

image1 = cv2.imread("img1.jfif")
image2 = cv2.imread("img2.jfif")
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

#ssim has two parameter i.e score and diff
(score,diff) = compare_ssim(gray1, gray2, full=True)
diff = (diff*255).astype("uint8")
print("SSIM: {}".format(score))
#The difference image is currently represented as a floating point data type in the range [0, 1] 
#so we first convert the array to 8-bit unsigned integers in the range [0, 255] 
#before we can further process it using OpenCV.

thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#we threshold our diff  image using both cv2.THRESH_BINARY_INV  and cv2.THRESH_OTSU — 
#both of these settings are applied at the same time using the vertical bar ‘or’ symbol, "|"
#A good threshold would be in the middle of those two values. 
#Similarly, Otsu's method determines an optimal global threshold value from the image histogram.

#now creating boundaries across the contours 
for c in cnts:
    (x,y,w,h) =  cv2.boundingRect(c)
    cv2.rectangle(image1,(x,y),(x+w,y+h), (0,0,255),2)
    cv2.rectangle(image2,(x,y),(x+w,y+h), (0,0,255),2)  
    
cv2.imshow("Image-1", image1)
cv2.imshow("Image-2", image2)
cv2.imshow("Difference Between Images", diff)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)








