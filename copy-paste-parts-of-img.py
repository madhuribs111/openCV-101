import cv2
import random
img = cv2.imread('assets/cloud.jpg', -1)

# numpy array slice: img[from1:to1, from2:to2]; from2 and to2 are in the range from1 and to1
tag = img[500:700, 600:900]
img[700:900, 600:900] = tag

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()