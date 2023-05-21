import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
from skimage import data

# Membaca gambar grayscale
image = cv2.imread('bogor.jpg', 0)#menampilkan gambar dengan nama file bogor.jpg

# Mengaplikasikan Histogram Equalization menggunakan cv2.equalizeHist()
equalized_image = cv2.equalizeHist(image)#Menggunakan fungsi cv2.equalizeHist() untuk menerapkan Histogram Equalization pada gambar

#Penerapan Metode Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))#Membuat objek CLAHE (Contrast Limited Adaptive Histogram Equalization) menggunakan fungsi cv2.createCLAHE(). Parameter clipLimit digunakan untuk mengatur batas kontras, dan tileGridSize mengatur ukuran grid tile.

#Apply CLAHE to the original image
image_clahe = clahe.apply(image)#Menggunakan objek CLAHE yang telah dibuat untuk menerapkan metode CLAHE pada gambar

#Penerapan metode Contrast Stretching (CS)
# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#Membuat array kosong dengan dimensi yang sama dengan gambar image untuk menyimpan gambar hasil dari metode Contrast Stretching (CS). Tipe data 'uint8' digunakan untuk mewakili nilai piksel dalam rentang 0-255.

# Apply Min-Max Contrasting
min = np.min(image)#untuk mendapatkan nilai piksel minimum dalam gambar
max = np.max(image)#untuk mendapatkan nilai piksel maksimum dalam gambar

for i in range(image.shape[0]):#Memulai loop untuk iterasi melalui setiap baris i
    for j in range(image.shape[1]):#Memulai loop untuk iterasi melalui setiap baris j
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)#perhitungan untuk menentukan di tiap baris dan kolom

#Penerapan Metode Perkalian Konstanta
copyCamera = image.copy().astype(float)#menduplikasikan array copyCitra1 kedalam variabel citra1 dengan tipe array float agar lebih presisi
m1,n1 = copyCamera.shape#ukuran array pada masing2 dimensi(baris dan kolom)
output1 = np.empty([m1, n1])#array kosong yang nantinya diisikan hasil operasi matematika

for baris in range(0, m1-1):#Memulai loop untuk iterasi melalui setiap baris gambar.
    for kolom in range(0, n1-1):#Memulai loop untuk iterasi melalui setiap kolom gambar.
        a1 = baris  # menyimpan nilai baris kedalam variable a1
        b1 = kolom  # menyimpan nilai baris kedalam variable b1
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9 #perhitungan untuk menentukan posisi plot yang ditampilkan

#Plot Image
fig, axes = plt.subplots(5, 2, figsize=(8, 8))#membuat plot 5 baris dan 2 kolom dengan ukuran foto 8x8
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(image, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[0].set_title("Citra Input")#membuat judul pada plot
ax[1].hist(image.ravel(), bins=256)#menampilkan gambar
ax[1].set_title('Histogram Input')#membuat judul pada plot

ax[2].imshow(equalized_image, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[2].set_title("Citra Output HE")#membuat judul pada plot
ax[3].hist(equalized_image.ravel(), bins=256)#menampilkan gambar
ax[3].set_title('Histogram Output HE Method')#membuat judul pada plot

ax[4].imshow(image_cs, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[4].set_title("Citra Output CS")#membuat judul pada plot
ax[5].hist(image_cs.ravel(), bins=256)#menampilkan gambar
ax[5].set_title('Histogram Output CS Method')#membuat judul pada plot

ax[6].imshow(image_clahe, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[6].set_title("Citra Grayscale CLAHE")#membuat judul pada plot
ax[7].hist(image_clahe.ravel(), bins=256)#menampilkan gambar
ax[7].set_title('Histogram Output CLAHE Method')#membuat judul pada plot

ax[8].imshow(output1, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#membuat judul pada plot
ax[9].hist(output1.ravel(), bins=256)#menampilkan gambar
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#membuat judul pada plot

fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot