
 import cv2 
# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("wafer_image.png", cv2.IMREAD_COLOR)
 

cv2.imshow("Cute Kitens", img)
 

cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()