import cv2
import numpy as np
import matplotlib.pyplot as plt
def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    center = (cols / 2, rows / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    return rotated_image

img = cv2.imread('bunga.jpg')#Baca gambar sumber
rotated_img = rotate_image(img, angle=-180)#Rotasi foto

cv2.imshow('Rotation Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()