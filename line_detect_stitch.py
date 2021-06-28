import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import os

# path = 'data/corn_seg/corn_0000090.png'
folder = 'data/corn_seg'
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))

    # img = cv2.imread(path)
    # img_org = cv2.imread(path)
    img_org = cv2.imread(os.path.join(folder, filename)) 
    # Displaying the image
    height, width = img.shape[:2]

    img = img[int(height/2):height,0:width]


    kernel = np.ones((37,37),np.uint8)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    # used img instead of closing
    edges = cv2.Canny(img,50,150,apertureSize = 3)
    minLineLength=100
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=50,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

    a,b,c = lines.shape
    weed_pos = []
    for i in range(a):
        # [0][0], and [0][2] are x (column locations)
        angle =  math.atan((lines[i][0][1]-lines[i][0][3])/(lines[i][0][0]-lines[i][0][2]))
        if  (angle > 1.3 and angle <= math.pi/2) or (angle < -1.3 and angle >= -math.pi/2) and abs((lines[i][0][1]-lines[i][0][3]))>100:
          cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
          #print(i,(lines[i][0][0], lines[i][0][2]))
          weed_pos.append(lines[i][0][0])
          weed_pos.append(lines[i][0][2])
    # plt.imshow(edges), plt.axis("off")
    weed_pos.sort()
    print(weed_pos)

    #plt.imshow(img), plt.axis("off")
    #plt.show()
    #plt.imshow(cropped_img), plt.axis("off")
    #plt.show()

    print(img.shape)
    print(img_org.shape)
    img_added = cv2.vconcat([img, img_org])
    cv2.imwrite(os.path.join('results', filename), img_added)
