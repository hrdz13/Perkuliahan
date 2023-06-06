#Import Liblary
import matplotlib.pyplot as plt
import cv2
import numpy as np

#membuat efek swirled dengan bantuan numpy
def swirled_effect(image, strength, radius):
    rows, cols = image.shape[:2]
    center_x, center_y = rows / 2, cols / 2
    map_x = np.zeros((rows, cols), dtype=np.float32)
    map_y = np.zeros((rows, cols), dtype=np.float32)

    for i in range(rows):
        for j in range(cols):
            x = j - center_x
            y = i - center_y
            theta = np.arctan2(y, x)
            distance = np.sqrt(x * x + y * y)
            if distance < radius:
                r = distance / radius
                angle = strength * (1 - r)
                map_x[i, j] = int(x * np.cos(angle) + y * np.sin(angle) + center_x)
                map_y[i, j] = int(-x * np.sin(angle) + y * np.cos(angle) + center_y)
            else:
                map_x[i, j] = j
                map_y[i, j] = i

    output = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    return output

img = cv2.imread('papancatur.png')#Membaca Gambar

output_img = swirled_effect(img, strength=10, radius=120)#mengaplikasikan efek swirled
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)
ax0.imshow(img, cmap=plt.cm.gray)
ax0.axis('off')
ax1.imshow(output_img, cmap=plt.cm.gray)
ax1.axis('off')
plt.show()