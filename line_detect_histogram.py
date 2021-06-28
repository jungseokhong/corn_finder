import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

# image file path
path = 'data/corn_seg/corn_0000090.png'

img = cv2.imread(path) 
height, width = img.shape[:2]
img = img[int(height/2):height,0:width]


# this is for image closing
kernel = np.ones((37,37),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# used img instead of closing
edges = cv2.Canny(img,50,150,apertureSize = 3)

# LineLength determined based on observation
minLineLength=100
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=50,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

a,b,c = lines.shape
weed_pos = []
cent_pos = []
for i in range(a):
    # [0][0], and [0][2] are x (column locations)
    angle =  math.atan((lines[i][0][1]-lines[i][0][3])/(lines[i][0][0]-lines[i][0][2]))
    # angle between 75 and 90 degree
    if  (angle > 1.3 and angle <= math.pi/2) or (angle < -1.3 and angle >= -math.pi/2) and abs((lines[i][0][1]-lines[i][0][3]))>100:
      cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
      #print(i,(lines[i][0][0], lines[i][0][2]))
      weed_pos.append(lines[i][0][0])
      weed_pos.append(lines[i][0][2])
      cent_pos.append((lines[i][0][0]+lines[i][0][2])/2.0)
# plt.imshow(edges), plt.axis("off")
weed_pos.sort()
cent_pos.sort()
cent_pos = np.array(cent_pos)
print(cent_pos)


plt.subplot(2,1,1)
plt.imshow(img), plt.axis("off")

plt.subplot(2,1,2)
# plt.hist(cent_pos, 848, range=[0,847])
a = plt.hist(cent_pos, 15, range=[0,847], align='mid')
plt.plot(a[1][1:], a[0])
plt.show()

#plt.imshow(cropped_img), plt.axis("off")
#plt.show()
# cv2.imwrite('test90.png', img)
