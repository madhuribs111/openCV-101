
import cv2
import random
img = cv2.imread('assets/cloud.jpg', -1)

# print(type(img)) = <class 'numpy.ndarray'>

# print(img.shape)=(1080, 1920, 3) 1080= height(rows), 1920= width(columns), 3= channels
# channels(number of values representing a pixel)

# RGB = standard pixel colors, but OpenCv= BGR

# [0,0,0] => Blue Green Red; from range: 0-255 (0-none, 255- all)

# change colors of pixel:

for i in range(100):
    for j in range(img.shape[1]):
        #modify entire column
        # randint(lower_bound, upper_bound)
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()