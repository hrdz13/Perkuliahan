import matplotlib.pyplot as plt#memanggil library matplotlib untuk mengolah array
from skimage import data#memanggil library data dari skimage untuk mengolah array
from skimage.io import imread#memanggil library imread dari skimage.io untuk mengolah array
from skimage.color import rgb2gray#memanggil library imread dari skimage.color untuk mengolah array
import numpy as np#memanggil library numpy untuk mengolah array

#Load & Plot Input Image
citra1 = imread(fname="mobil.tif")#menampilkan gambar dengan nama file mobil.tif
citra2 = imread(fname="boneka2.tif")#menampilkan gambar dengan nama file boneka2.tif

print('Shape citra 1 : ', citra1.shape)#menampilkan output nilai
print('Shape citra 1 : ', citra2.shape)#menampilkan output nilai

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#membuat plot 1 baris dan 2 kolom dengan ukuran foto 10x10
ax = axes.ravel()#menyusun plot ke dalam bentuk array


ax[0].imshow(citra1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[0].set_title("Citra 1")#membuat judul pada plot
ax[1].imshow(citra2, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[1].set_title("Citra 2")#membuat judul pada plot
plt.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar

#Menyiapkan variable output
copyCitra1 = citra1.copy()#membuat salinan data dari variable citra1
copyCitra2 = citra2.copy()#membuat salinan data dari variable citra2

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


for baris in range(0, m1 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk baris
    for kolom in range(0, n1 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk kolom
        a1 = baris  # menyimpan nilai baris kedalam variable a1
        b1 = kolom  # menyimpan nilai baris kedalam variable b1

        # perhitungan untuk menentukan posisi plot yang ditampilkan
        arr = np.array([copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1, b1 + 1], \
                        copyCitra1[a1, b1 - 1], copyCitra1[a1, b1 + 1], copyCitra1[a1 + 1, b1 - 1], \
                        copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]])

        minPiksel = np.amin(arr);#menentukan nilai min
        maksPiksel = np.amax(arr);#menentukan nilai max

        if copyCitra1[baris, kolom] < minPiksel:#Memeriksa apakah nilai piksel pada posisi (baris, kolom) dalam gambar copyCitra1 lebih kecil dari minPiksel. Jika ya, dilakukan pernyataan berikutnya.
            output1[baris, kolom] = minPiksel#Set nilai piksel pada posisi (baris, kolom) di gambar hasil (output1) menjadi maksPiksel.
        else:
            if copyCitra1[baris, kolom] > maksPiksel:#Memeriksa apakah nilai piksel pada posisi (baris, kolom) dalam gambar copyCitra1 lebih besar dari minPiksel. Jika ya, dilakukan pernyataan berikutnya.
                output1[baris, kolom] = maksPiksel#Set nilai piksel pada posisi (baris, kolom) di gambar hasil (output1) menjadi maksPiksel.
            else:
                output1[baris, kolom] = copyCitra1[baris, kolom]#Set nilai piksel pada posisi (baris, kolom) di gambar hasil menjadi copyCitra1

#Proses Filter Batas Pada Citra Input 2
for baris1 in range(0, m2 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk baris1
    for kolom1 in range(0, n2 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk kolom1

        a1 = baris1# menyimpan nilai baris kedalam variable a1
        b1 = kolom1# menyimpan nilai baris kedalam variable b1

        # perhitungan untuk menentukan posisi plot yang ditampilkan
        arr = np.array([copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1, b1 + 1], \
                        copyCitra2[a1, b1 - 1], copyCitra2[a1, b1 + 1], copyCitra2[a1 + 1, b1 - 1], \
                        copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]])

        minPiksel = np.amin(arr);#menentukan nilai min
        maksPiksel = np.amax(arr);#menentukan nilai maks

        if copyCitra2[baris1, kolom1] < minPiksel:#Memeriksa apakah nilai piksel pada posisi (baris, kolom) dalam gambar copyCitra1 lebih kecil dari minPiksel. Jika ya, dilakukan pernyataan berikutnya.
            output2[baris1, kolom1] = minPiksel#Set nilai piksel pada posisi (baris, kolom) di gambar hasil (output1) menjadi maksPiksel.
        else:
            if copyCitra2[baris1, kolom1] > maksPiksel:#Memeriksa apakah nilai piksel pada posisi (baris, kolom) dalam gambar copyCitra1 lebih besar dari minPiksel. Jika ya, dilakukan pernyataan berikutnya.
                output2[baris1, kolom1] = maksPiksel#Set nilai piksel pada posisi (baris, kolom) di gambar hasil (output1) menjadi maksPiksel.
            else:
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]#Set nilai piksel pada posisi (baris, kolom) di gambar hasil menjadi copyCitra2

#Plot Citra Input dan Output Hasil dari Filter Batas
fig, axes = plt.subplots(2, 2, figsize=(10, 10))#membuat plot 2 baris dan 2 kolom dengan ukuran foto 10x10
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(citra1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[0].set_title("Input Citra 1")#membuat judul pada plot

ax[1].imshow(citra2, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[1].set_title("Input Citra 2")#membuat judul pada plot

ax[2].imshow(output1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[2].set_title("Output Citra 1")#membuat judul pada plot

ax[3].imshow(output2, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[3].set_title("Output Citra 2")#membuat judul pada plot

plt.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar