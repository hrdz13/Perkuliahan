import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt
import numpy as np#memanggil library numpy untuk mengolah array
import cv2#memanggil library cv2 untuk mengolah gambar

#Percobaan 1 - Cropping Image
# membaca gambar
image = cv2.imread('Bogor.jpg')#membaca gambar dengan nama Bogor.jpg dan menyimpannya ke dalam variable image
image1 = cv2.imread('citra.jpg')#membaca gambar dengan nama citra.jpg dan menyimpannya ke dalam variable image1

#memotong gambar
cropped = image[100:100+200, 100:100+200]
cropped2 = image1[100:100+200, 100:100+200]

#menampilkan gambar yang telah dipotong
fig, axes = plt.subplots(ncols=2, nrows=2)#membuat plot dengan dua kolom dan dua baris
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(image)#menampilkan gambar
ax[0].set_title("Citra Asli")#memberikan judul pada plot
ax[1].imshow(cropped)#menampilkan gambar croppped
ax[1].set_title("Crop 1")#memberikan judul pada plot
ax[2].imshow(image1)#menampilkan gambar image1
ax[2].set_title("Citra Asli 2")#memberikan judul pada plot
ax[3].imshow(cropped2)#menampilkan gambar cropped2
ax[3].set_title("Crop 2")#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

#Percobaan 2 - Citra Negative
inv = 255 - cropped2 #rumus untuk mengkonversi gambar menjadi citra negatif
print('Shape Input : ', cropped.shape)#menampilkan keluaran gambar crop dengan judul Share input
print('Shape Output : ',inv.shape)#menampilkan keluaran gambar crop dengan judul Share output

fig, axes = plt.subplots(ncols=2, nrows=2)#membuat plot dengan dua kolom dan dua baris
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(cropped)#menampilkan gambar
ax[0].set_title("Citra Input")#memberikan judul pada plot
ax[1].hist(cropped.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[1].set_title('Histogram Input')#memberikan judul pada plot
ax[2].imshow(inv)#menampilkan gambar
ax[2].set_title('Citra Output (Inverted Image)')#memberikan judul pada plot
ax[3].hist(inv.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[3].set_title('Histogram Output')#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

gambar2=cropped2.copy().astype(float)#menduplikasikan array cropped2 kedalam variabel gambar2 dengan tipe array float agar lebih presisi
m1, n1 = gambar2.shape#ukuran array pada masing2 dimensi(baris dan kolom)
output1 = np.empty([m1, n1])#array kosong yang nantinya diisikan hasil operasi matematika

for baris in range(0, m1 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk baris
    for kolom in range(0, n1 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk kolom
        a1 = baris#menyimpan nilai baris kedalam variable a1
        b1 = kolom#menyimpan nilai kolom kedalam variable b1
        output1[a1, b1] = gambar2[baris, kolom] + 100#menambahkan nilai 100 pada piksel baris dan kolom pada output untuk citra hasil informasi

fig, axes = plt.subplots(ncols=2, nrows=2)#membuat plot dengan dua kolom dan dua baris
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(cropped2, cmap='gray')#menampilkan gambar kedalam bentuk grayscale
ax[0].set_title("Citra Input")#memberikan judul pada plot
ax[1].hist(cropped.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[1].set_title('Histogram Input')#memberikan judul pada plot
ax[2].imshow(output1, cmap='gray')#menampilkan gambar kedalam bentuk grayscale
ax[2].set_title('Citra Output (Brightnes)')#memberikan judul pada plot
ax[3].hist(output1.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[3].set_title('Histogram Input')#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot
