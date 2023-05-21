import matplotlib.pyplot as plt#memanggil library matplotlib untuk mengolah array
from skimage import data#memanggil library data dari skimage untuk mengolah array
from skimage.io import imread#memanggil library imread dari skimage.io untuk mengolah array
from skimage.color import rgb2gray#memanggil library imread dari skimage.color untuk mengolah array
import numpy as np#memanggil library numpy untuk mengolah array
import cv2#memanggil library cv2 untuk mengolah array

citra1 = imread(fname="gedung.tif")#menampilkan gambar dengan nama file gedung.tif
print(citra1.shape)#mencetak ukuran gambar

plt.imshow(citra1, cmap='gray')#menampilkan gambar dengan scala gray

#Proses Konvolusi
#Membuat sebuah matriks kernel sebagai filter konvolusi. Kernel ini memiliki ukuran 3x3 dan memiliki nilai tertentu untuk setiap elemennya. Kernel ini akan digunakan untuk melakukan operasi konvolusi pada citra.
kernel = np.array([[-1, 0, -1],
                   [0, 4, 0],
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)#Menggunakan fungsi cv2.filter2D untuk menerapkan operasi konvolusi pada citra citra1 menggunakan kernel yang telah ditentukan. Hasil dari operasi konvolusi akan disimpan dalam variabel citraOutput. Parameter -1 menandakan bahwa tipe output akan sama dengan tipe input citra.

fig, axes = plt.subplots(1, 2, figsize=(12, 12))#membuat plot 1 baris dan 2 kolom dengan ukuran foto 12x12
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(citra1, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[0].set_title("Citra Input")#membuat judul pada plot
ax[1].imshow(citraOutput, cmap = 'gray')#menampilkan gambar dengan tipe gray
ax[1].set_title("Citra Output")#membuat judul pada plot
plt.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar