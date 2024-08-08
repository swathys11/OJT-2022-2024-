import cv2 
import numpy as np

#read the image with the particulr library which we have  imported
image = cv2.imread("traffic signal.jpg")

if image is None:
    print("Could not read the image")
    exit()

#original image
cv2.imshow('original image', image)
cv2.waitKey(0)


#convert to grayscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale image: ", grey_image)
cv2.waitKey(0)


#apply a guassian blur into the above image
blur_img = cv2.GaussianBlur(grey_image, (5,5), 0)
cv2.imshow("Blurred image ", blur_img)
cv2.waitKey(0)


#Edge detection by using canny in cv2
edges = cv2.Canny(blur_img, 50, 150)
cv2.imshow(" Edged image ", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

