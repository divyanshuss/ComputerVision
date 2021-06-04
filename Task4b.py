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

cropfl1 = flower1[:699 , 255: -256]
cropfl1a = cropfl1[: , 312: ]
cv2.imshow("f1" , cropfl1a)
cv2.waitKey()
cv2.destroyAllWindows()
cropf2 = flower2[:699 , : ]
cropf2a=cropf2[: , : 312]
cv2.imshow("f1" , cropf2a)
cv2.waitKey()
cv2.destroyAllWindows()
fl12=numpy.hstack((cropfl1a , cropf2a))
cv2.imshow("f1" , fl12)
cv2.waitKey()
cv2.destroyAllWindows()


# Cropping Image and paste over other

photo = cv2.imread("IMG_20200203_145021.jpg")
cv2.imshow("pic", photo)
cv2.waitKey()
cv2.destroyAllWindows()
cropimg = photo[40:360 , 90:640]
cv2.imshow("pic", cropimg)
cv2.waitKey()
cv2.destroyAllWindows()
photo2 = cv2.imread("Snap.jpg")
cv2.imshow("pic", photo2)
cv2.waitKey()
cv2.destroyAllWindows()
photo2[40:360 , 90:640] = cropimg
cv2.imshow("pic", photo2)
cv2.waitKey()
cv2.destroyAllWindows()
photo2[40:360 , 90:640] = cropimg
cv2.imshow("pic", photo2)
cv2.waitKey()
cv2.destroyAllWindows()
