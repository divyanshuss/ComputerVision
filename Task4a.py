# TASK  : Take two images and combine them to form one image.
import cv2
import numpy
flower1 = cv2.imread("a.jpg")
flower2 = cv2.imread("b.jpg")

#Show original flower1
cv2.imshow("flw1" , flower1)
cv2.waitKey()
cv2.destroyAllWindows
 #Show original flower2
cv2.imshow("flw1" , flower2)
cv2.waitKey()
cv2.destroyAllWindows


#Crop the flower1
cropfl1 = flower1[:699 , 255: -256]
cv2.imshow("f1" , cropfl1)
cv2.waitKey()
cv2.destroyAllWindows()

#Crop the flower2
cropf2 = flower2[:699 , : ]
cv2.imshow("f1" , cropf2)
cv2.waitKey()
cv2.destroyAllWindows()

#Combine the two flowers
fl12=numpy.hstack((cropfl1 , cropf2))
cv2.imshow("f1" , fl12)
cv2.waitKey()
cv2.destroyAllWindows()
