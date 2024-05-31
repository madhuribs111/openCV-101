import cv2

# load an image :(blue, green red) color pattern is default loading of cv2
# load it with greyscale, transparency (mode)
# -1, cv2.IMREAD_COLOR : loads a color image. Any transparancy of image will be neglected
# 0, cv2.IMREAD_GREYSCALE : Loads image in grayscale mode
# 1,cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv2.imread('./cloud.jpg', 1)
# resize image; (0,0)= your own fx and fy values. fx, fy: axes
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# rotate an image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_img.jpg', img)
cv2.imshow('image', img)
# wait 0 - infinitely so that when we press any key window is destroyed
# cv2.waitKey(10) - wait for 1 second
cv2.waitKey(0)
cv2.destroyAllWindows()
