# TASK 4.1 : CREATE your own image 

import cv2
import numpy
img = numpy.zeros((400,600,3),numpy.uint8)
cv2.imshow("pic" , img)
cv2.waitKey()
cv2.destroyAllWindows()
img [10] = [0,255,0]
img [20] = [0,255,0]
img [30] = [0,255,0]
img [40] = [0,255,0]
img [50] = [0,255,0]
img [70] = [0,255,0]
img [80] = [0,255,0]
img [90] = [0,255,0]

img [310] = [0,0,255] 
img [320] = [0,0,255] 
img [330] = [0,0,255]
img [340] = [0,0,255] 
img [350] = [0,0,255]
img [360] = [0,0,255] 
img [370] = [0,0,255]
img [380] = [0,0,255] 
img [390] = [0,0,255]
cv2.imshow("pic" , img)
cv2.waitKey()
cv2.destroyAllWindows()
img1 = cv2.rectangle(img ,(100 ,200) ,(300, 300), [255, 0, 0] , -1)
cv2.imshow("pic" , img1)
cv2.waitKey()
cv2.destroyAllWindows()
img2= cv2.circle(img , (300,200) , 100, [225 ,57,244] , -1)
cv2.imshow("pic" , img2)
cv2.waitKey()
cv2.destroyAllWindows()
font = cv2.FONT_HERSHEY_SIMPLEX
org = (300, 200)
fontScale = 1
color = (13,255, 255,)
thickness = 2
image3 = cv2.putText(img, 'HALLO', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("pic" , image3)
cv2.waitKey()
cv2.destroyAllWindows()
