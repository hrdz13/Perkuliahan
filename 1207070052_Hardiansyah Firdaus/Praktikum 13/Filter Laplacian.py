import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bunga.jpg')#Baca gambar sumber
#Konversi ke Grey
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Hilangkan Noise
img0 = cv2.GaussianBlur(gray, (3, 3), 0)
#konvolusi dengan kernel
laplacian = cv2.Laplacian(img0, cv2.CV_64F)
#Tampilkan dengan Matplolib
plt.subplots(121)
plt.imshow(img0, cmap= 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplots(122)
plt.imshow(laplacian, cmap= 'gray')
plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.show()