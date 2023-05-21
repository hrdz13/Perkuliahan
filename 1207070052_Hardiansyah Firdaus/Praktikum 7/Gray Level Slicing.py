import cv2#memanggil library cv2 untuk mengolah array
import numpy as np#memanggil library numpy untuk mengolah array
import matplotlib.pyplot as plt#memanggil library matplotlib untuk mengolah array

img = image = cv2.imread('sukabumi.jpg', 0)#untuk membaca gambar "sumedang.jpg" dalam mode grayscale (nilai 0).

row, column = img.shape #Menggunakan metode .shape pada data img untuk mendapatkan dimensi gambar.

img1 = np.zeros((row, column), dtype='uint8')#Membuat matriks nol dengan dimensi yang sama dengan gambar awal. Matriks ini akan digunakan untuk menyimpan gambar hasil transformasi. Tipe data 'uint8' digunakan untuk mewakili nilai piksel dalam rentang 0-255.

min_range = 10#Menetapkan nilai batas bawah (minimum) untuk transformasi biner.
max_range = 60#Menetapkan nilai batas atas (Maximum) untuk transformasi biner.

for i in range(row):#Memulai loop untuk iterasi melalui setiap baris gambar.
    for j in range(column):#Memulai loop nested untuk iterasi melalui setiap kolom gambar.
        if img[i, j] > min_range and img[i, j] < max_range:#Memeriksa apakah nilai piksel pada posisi (i, j) dalam rentang yang ditentukan.
            img1[i, j] = 255#Jka piksel memenuhi syarat, set nilai piksel pada posisi (i, j) di gambar hasil (img1) menjadi 255 (putih).
        else:
            img1[i, j] = 0#Set nilai piksel pada posisi (i, j) di gambar hasil (img1) menjadi 0 (hitam).

fig, axes = plt.subplots(2, 2, figsize=(12, 12))#membuat plot 2 baris dan 2 kolom dengan ukuran foto 12x12
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(img, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[0].set_title("Citra Input")#membuat judul pada plot
ax[1].hist(img.ravel(), bins=256)#menampilkan histogram pada gambar
ax[1].set_title('Histogram Input')#membuat judul pada plot

ax[2].imshow(img1, cmap=plt.cm.gray)#menampilkan gambar dengan tipe gray
ax[2].set_title("Citra Output")#membuat judul pada plot
ax[3].hist(img1.ravel(), bins=256)#menampilkan histogram pada gambar
ax[3].set_title('Histogram Output')#membuat judul pada plot

fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot