import numpy as np
from skimage.io import imshow, imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import cv2

sample = imread('frame000000.png')
sample_g = rgb2gray(sample)

fig, ax = plt.subplots(1,3,figsize=(15,5))
sample_b = sample_g > 0.6
ax[0].set_title('Grayscale Image',fontsize=20)
ax[0].imshow(sample[:,:,1])
ax[1].plot(sample_g[300])
ax[1].set_ylabel('Pixel Value')
ax[1].set_xlabel('Width of Picture')
ax[1].set_title('Plot of 1 Line',fontsize=15)
ax[2].set_title('Binarized Image',fontsize=15)
ax[2].imshow(sample_b,cmap='gray')

plt.show()

## Read
img = cv2.imread("color_0000000.png")

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

## slice the green
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## save 
cv2.imwrite("green1.png", green)