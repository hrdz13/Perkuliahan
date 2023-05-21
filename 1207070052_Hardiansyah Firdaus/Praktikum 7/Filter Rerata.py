import cv2#memanggil library cv2 untuk mengolah array
import numpy as np#memanggil library numpy untuk mengolah array
import matplotlib.pyplot as plt#memanggil library matplotlib untuk mengolah array
from skimage import data#memanggil library data dari skimage untuk mengolah array
from skimage.io import imread#memanggil library imread dari skimage.io untuk mengolah array
from skimage.color import rgb2gray#memanggil library imread dari skimage.color untuk mengolah array

citra1 = imread(fname="boneka2.tif")#menampilkan gambar dengan nama file boneka2.tif
citra2 = imread(fname="mobil.tif")#menampilkan gambar dengan nama file mobil.tif

print('Shape citra 1 : ', citra1.shape)#menampilkan output nilai
print('Shape citra 2 : ', citra2.shape)#menampilkan output nilai

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#membuat plot 1 baris dan 2 kolom dengan ukuran foto 12x12
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(citra1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[0].set_title("Citra 1")#membuat judul pada plot
ax[1].imshow(citra2, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[1].set_title("Citra 2")#membuat judul pada plot

fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

copyCitra1 = citra1.copy().astype(float)#menduplikasikan array copyCitra1 kedalam variabel citra1 dengan tipe array float agar lebih presisi
copyCitra2 = citra2.copy().astype(float)#menduplikasikan array copyCitra2 kedalam variabel citra2 dengan tipe array float agar lebih presisi

m1,n1 = copyCitra1.shape#ukuran array pada masing2 dimensi(baris dan kolom)
output1 = np.empty([m1, n1])#array kosong yang nantinya diisikan hasil operasi matematika

m2,n2 = copyCitra2.shape#ukuran array pada masing2 dimensi(baris dan kolom)
output2 = np.empty([m2, n2])#array kosong yang nantinya diisikan hasil operasi matematika
print('Shape copy citra 1 : ', copyCitra1.shape)#menampilkan output nilai
print('Shape output citra 1 : ', output1.shape)#menampilkan output nilai

print('m1 : ',m1)#menampilkan output nilai
print('n1 : ',n1)#menampilkan output nilai
print()#membuat baris baru

print('Shape copy citra 2 : ', copyCitra2.shape)#menampilkan output nilai
print('Shape output citra 3 : ', output2.shape)#menampilkan output nilai
print('m2 : ',m2)#menampilkan output nilai
print('n2 : ',n2)#menampilkan output nilai
print()#membuat baris baru

for baris in range(0, m1-1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk baris
    for kolom in range(0, n1-1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk kolom
        a1 = baris#menyimpan nilai baris kedalam variable a1
        b1 = kolom#menyimpan nilai baris kedalam variable b1
        #perhitungan untuk menentukan posisi plot yang ditampilkan
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1];
        output1[a1, b1] = (1/9 * jumlah)

for baris1 in range(0, m2-1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk baris
    for kolom1 in range(0, n2-1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk kolom
        a1 = baris1#menyimpan nilai baris kedalam variable a1
        b1 = kolom1#menyimpan nilai baris kedalam variable b1

        # perhitungan untuk menentukan posisi plot yang ditampilkan
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1];
        output2[a1, b1] = (1/9 * jumlah)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))#membuat plot 2 baris dan 2 kolom dengan ukuran foto 10x10
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(citra1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[0].set_title("Input Citra 1")#membuat judul pada plot

ax[1].imshow(citra2, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[1].set_title("Input Citra 1")#membuat judul pada plot

ax[2].imshow(output1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[2].set_title("Output Citra 1")#membuat judul pada plot

ax[3].imshow(output2, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[3].set_title("Output Citra 2")#membuat judul pada plot

fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot