import numpy as np
import cv2
import imageio
import matplotlib.pyplot as plt
img = cv2.imread('gunung.jpg')

#define reso dan tipe gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

#Percobaan pertama kita buat brightness untuk gambar gray scale
#membuat variable img_brightness untuk menampung

img_brightness = np.zeros(img.shape, dtype=np.uint8)

#membuat fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai) :
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue))/3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)

fig, axes = plt.subplots(ncols=2)
ax = axes.ravel()
brighter(-100)
ax[0].imshow(img_brightness)
ax[0].set_title("Brighness -100")
brighter(50)
ax[1].imshow(img_brightness)
ax[1].set_title("Brighness 50")
fig.tight_layout()
plt.show()

#brightness RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_brightness[y][x] = (red, green, blue)
fig, axes = plt.subplots(ncols=2)
ax = axes.ravel()
rgbbrighter(-100)
ax[0].imshow(img_brightness)
ax[0].set_title("Brighness -100")
rgbbrighter(100)
ax[1].imshow(img_brightness)
ax[1].set_title("Brighness 100")
fig.tight_layout()
plt.show()

#contrast
img_contrass = np.zeros(img.shape, dtype=np.uint8)

def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)

fig, axes = plt.subplots(ncols=2)
ax = axes.ravel()
contrass(50)
ax[0].imshow(img_contrass)
ax[0].set_title("Contrass 50")
contrass(100)
ax[1].imshow(img_contrass)
ax[1].set_title("Contrass 100")
fig.tight_layout()
plt.show()


#Brightness Contrass RGB
img_rgbcontrass = np.zeros(img.shape, dtype=np.uint8)

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            img_rgbcontrass[y][x] = (red, green, blue)
fig, axes = plt.subplots(ncols=2)
ax = axes.ravel()
rgbcontrass(50)
ax[0].imshow(img_rgbcontrass)
ax[0].set_title("Contrass 50")
rgbcontrass(100)
ax[1].imshow(img_rgbcontrass)
ax[1].set_title("Contrass 100")
fig.tight_layout()
plt.show()