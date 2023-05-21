# memanggil modul yang diperlukan
import cv2#memanggil library cv2 untuk mengolah array
import numpy as np#memanggil library numpy untuk mengolah array
from matplotlib import pyplot as plt #memanggil library matplotlib untuk mengolah array

#bgr
img = cv2.imread('dog.jpg')#menampilkan gambar dog

#rgb
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#untuk mengubah mode warna gambar dari BGR (Blue-Green-Red) menjadi RGB (Red-Green-Blue)

# tampilkan gambar awal tanpa filter
cv2.imshow('foto asli', img)#menampilkan gambar asli
cv2.waitKey(0)#Menunggu tombol keyboard ditekan sebelum menutup jendela gambar.
cv2.destroyAllWindows()#Menutup semua jendela gambar yang terbuka.

# membuat filter: matriks berukuran 5 x 5
kernel = np.ones((5,5),np.float32)/25#Membuat filter dengan menggunakan matriks 5 x 5 yang terdiri dari elemen-elemen bernilai 1
print(kernel)#menampilkan hasil dari variabel kernel

# lakukan filtering
Anjing_filter = cv2.filter2D(img,-1,kernel)#Melakukan filtering pada gambar img menggunakan fungsi cv2.filter2D.

cv2.imshow('Kucing Filter', Anjing_filter)#menampilkan gambar hasil filtering
cv2.waitKey(0)#Menunggu tombol keyboard ditekan sebelum menutup jendela gambar.
cv2.destroyAllWindows()#Menutup semua jendela gambar yang terbuka.

# salt and pepper

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15,15)#Menetapkan ukuran gambar plot menjadi (15, 15) menggunakan rcParams dari matplotlib.

# plot pertama, gambar asli
plt.subplot(121),plt.imshow(cat),plt.title('Original')#membuat subplot pertama dengan data cat, dengan judul plot Original
plt.xticks([]), plt.yticks([])#Menghilangkan penanda sumbu x dan y pada subplot kedua

# kedua, hasil filter
plt.subplot(122),plt.imshow(Anjing_filter)#membuat subplot pertama dengan data cat
plt.title('Averaging')#membuat judul plot
plt.xticks([]), plt.yticks([])#Menghilangkan penanda sumbu x dan y pada subplot kedua

# Plot!
plt.show()#menampilkan semua plot

Anjing_blur = cv2.blur(img,(5,5))# untuk menerapkan filter blur pada gambar img dengan ukuran kernel (5,5)

cv2.imshow('Anjing Blur', Anjing_blur)#Menampilkan gambar hasil blur dengan judul "Anjing Blur"
cv2.waitKey(0)#Menunggu tombol keyboard ditekan sebelum menutup jendela gambar.
cv2.destroyAllWindows()#Menutup semua jendela gambar yang terbuka.

# ini adalah cara lain untuk membuat sebuah kernel,
# yaitu dengan menggunakan np.matrix
# kali ini, ukuran matriksnya 3 x 3
kernel = np.matrix([#Membuat matriks kernel dengan menggunakan np.matrix. Baris ini menunjukkan inisialisasi kernel dengan elemen-elemen yang diberikan.
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ])/25
print(kernel)#menampilkan data

# buat lagi filteringnya
Anjing_filter = cv2.filter2D(img,-1,kernel)#Menggunakan fungsi cv2.filter2D untuk menerapkan operasi filter pada gambar img. Hasilnya disimpan dalam variabel Anjing_filter.

# tampilkan
cv2.imshow('Anjing Filter', Anjing_filter)#menampilkan gambar dengan judul Anjing Filter
cv2.waitKey(0)#Menunggu tombol keyboard ditekan sebelum menutup jendela gambar.
cv2.destroyAllWindows()#Menutup semua jendela gambar yang terbuka.

#High-Pass Filtering
# Highpass Filter

# sebenarnya kita tidak perlu melakukan filtering lagi. Cukup sekali saja
# di bagian awal, selama notebook ini tetap terhubung
import cv2#memanggil library cv2 untuk mengolah array
import numpy as np#memanggil library numpy untuk mengolah array
from matplotlib import pyplot as plt#memanggil library matplotlib untuk mengolah array

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('ml.jpg',0)#menampilan gambar ml.jpg

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)#untuk menghitung operasi laplacian pada gambar img. Hasilnya disimpan dalam variabel laplacian.

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)#untuk menghitung operasi sobel pada gambar img dalam arah x (horizontal).
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)#untuk menghitung operasi sobel pada gambar img dalam arah y (vertical).

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (10,10)#Mengatur ukuran default untuk gambar plot menggunakan liblary dengan satuan inch

# menampilkan hasil filter
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')#membuat subplot pertama dengan skala warna gray
plt.title('Original'), plt.xticks([]), plt.yticks([])#membuat judul, Menghilangkan tanda sumbu x dan y pada subplot pertama.
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')#membuat subplot kedua dengan skala warna gray
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])#membuat judul, Menghilangkan tanda sumbu x dan y pada subplot kedua.
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')#membuat subplot ketiga dengan skala warna gray
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])#membuat judul, Menghilangkan tanda sumbu x dan y pada subplot ketiga.
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')#membuat subplot keempat dengan skala warna gray
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])#membuat judul, Menghilangkan tanda sumbu x dan y pada subplot keempat.
plt.show()#menampilkan semua plot

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('pubg.jpeg',0)#menampilkan gambar pubg

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)#untuk mendeteksi tepi pada gambar img dengan menggunakan nilai threshold 100 dan 200.

plt.subplot(121),plt.imshow(img,cmap = 'gray')#membuat subplot pertama dengan skala warna gray
plt.title('Original Image'), plt.xticks([]), plt.yticks([])#membuat judul, Menghilangkan tanda sumbu x dan y pada subplot pertama.
plt.subplot(122),plt.imshow(edges,cmap = 'gray')#membuat subplot kedua dengan skala warna gray
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])#membuat judul, Menghilangkan tanda sumbu x dan y pada subplot kedua.
plt.show()#menampilkan semua plot

#Image Thresholding
# membaca gambar baymax
img = cv2.imread('pubg.jpeg',0)#menampilkan gambar

# Hitungan threshold.
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi
# yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#Menerapkan thresholding binary pada gambar img. Nilai piksel yang lebih besar dari 127 akan diubah menjadi 255 (putih), sementara nilai piksel yang lebih kecil atau sama dengan 127 akan diubah menjadi 0 (hitam).
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#Menerapkan thresholding binary pada gambar img. Nilai piksel yang lebih besar dari 127 akan diubah menjadi 255 (putih), sementara nilai piksel yang lebih kecil atau sama dengan 127 akan diubah menjadi 0 (hitam).
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#Menerapkan thresholding binary pada gambar img. Nilai piksel yang lebih besar dari 127 akan diubah menjadi 255 (putih), sementara nilai piksel yang lebih kecil atau sama dengan 127 akan diubah menjadi 0 (hitam).
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#Menerapkan thresholding binary pada gambar img. Nilai piksel yang lebih besar dari 127 akan diubah menjadi 255 (putih), sementara nilai piksel yang lebih kecil atau sama dengan 127 akan diubah menjadi 0 (hitam).
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)#Menerapkan thresholding binary pada gambar img. Nilai piksel yang lebih besar dari 127 akan diubah menjadi 255 (putih), sementara nilai piksel yang lebih kecil atau sama dengan 127 akan diubah menjadi 0 (hitam).

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']#membuat judul untuk plot
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]#memanggil variable untuk dimasukan kedalam plot

# menampilkan beberapa gambar sekaligus
for i in range(6):##perulangan untuk mengintegrasikan setiap baris pada gambar untuk baris
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')#membuat plot pertama dengan judul plot gray
    plt.title(titles[i])#memanggil semua judul
    plt.xticks([]),plt.yticks([])#Menghilangkan tanda sumbu x dan y pada subplot kedua.
plt.show()#menampilkan semua plot

# masih menggunakan variabel img yang sama
#img = cv2.imread('images/baymax.jpg',0)

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
img = cv2.medianBlur(img,5)#menampilkan gambar dengan filter median blur

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#Menggunakan fungsi cv2.threshold untuk melakukan thresholding pada gambar img dengan menggunakan metode thresholding binary.

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)#Menggunakan fungsi cv2.adaptiveThreshold untuk melakukan thresholding adaptif pada gambar img dengan menggunakan metode rata-rata (mean).

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)#Menggunakan fungsi cv2.adaptiveThreshold untuk melakukan thresholding adaptif pada gambar img dengan menggunakan metode rata-rata (mean).


# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']#membuat judul untuk semua plot
images = [img, th1, th2, th3]#memanggil variable untuk semua plot

# menampilkan hasil
for i in range(4):#membuat perulangan sebanyak 4
    plt.subplot(2,2,i+1)#membuat plot pertama dengan judul plot gray
    plt.imshow(images[i],'gray')#menampilkan semua gambar pada plot dengan judul gray
    plt.title(titles[i])#menampilkan semua judul
    plt.xticks([]),plt.yticks([])#Menghilangkan tanda sumbu x dan y pada subplot kedua.
plt.show()#menampilkan semua plot