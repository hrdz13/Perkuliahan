import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bunga.jpg')#Baca gambar sumber

#Filter Canny
img_canny = cv2.Canny(img, 100, 200)

#Plot Ouput
fig, axes= plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

ax[0].imshow(img, cmap = 'gray')
ax[0].set_title("Citra Input")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title("Histogram Citra Input")

ax[2].imshow(img_canny, cmap = 'gray')
ax[2].set_title("Citra Output")
ax[3].hist(img.ravel(), bins=256)
ax[3].set_title("Histogram Citra Output")

fig.tight_layout()
plt.show()