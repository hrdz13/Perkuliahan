import numpy as np#memanggil library numpy untuk mengolah array
import imageio#memanggil library imageio untuk mengolah array
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt

img = imageio.imread("sunset.jpg")#membaca gambar dengan nama sunset.jpg dan menyimpannya ke dalam variable image

img_height = img.shape[0] #membuat variable tinggi gambar dan menyimpannya ke dalam variable img_height
img_width = img.shape[1] #membuat variable lebar gambar dan menyimpannya ke dalam variable img_width
img_channel = img.shape[2] #membuat variable channel gambar dan menyimpannya ke dalam variable img_channel

#Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):#mendefinisikan sebuah fungsi Python yang bernama inversi_grayscale dengan satu parameter masukan nilai
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = nilai - gray #mengurangi nilai dengan gray
            img_inversi[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_inversi

#Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai):#mendefinisikan sebuah fungsi Python yang bernama inversi_grayscale dengan satu parameter masukan nilai
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            red = nilai - red#mengurangi nilai dengan red
            green = img[y][x][1]# mengambil nilai piksel green pada titik (y,x)
            green = nilai - green#mengurangi nilai dengan green
            blue = img[y][x][2]# mengambil nilai piksel blue pada titik (y,x)
            blue = nilai - blue#mengurangi nilai dengan blue
            img_inversi[y][x] = (red, green, blue)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_inversi

#Menampilkan hasil inversi
inversi_grayscale(255)#melakukan konversi ke inversi pada variable inversi_grayscale
plt.imshow(img_inversi)#menampilkan gambar
plt.title("Inversi Grayscale")#membuat judul pada plot
plt.show()#menampilkan plot

inversi_rgb(255)#melakukan konversi ke inversi pada variable inversi_rgb
plt.imshow(img_inversi)#menampilkan gambar
plt.title("Inversi RGB")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Mendefinisikan fungsi untuk log
def log(c):#mendefinisikan sebuah fungsi Python yang bernama log dengan satu parameter masukan c
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = int(c * np.log(gray + 1)) #perhitungan untuk menampilkan data log
            if gray > 255: #mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:#mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_log[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_log

#Menampilkan hasil log
log(30)#mengatur nilai log
plt.imshow(img_log)#menampilkan gambar
plt.title("Log")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Mendefinisikan fungsi untuk inversi log
def inlog(c):#mendefinisikan sebuah fungsi Python yang bernama inlog dengan satu parameter masukan c
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = int(c * np.log(255 - gray + 1))#perhitungan untuk menampilkan data inlog
            if gray > 255:  # mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:  # mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_inlog
#Menampilkan hasil inversi log
inlog(30)#mengatur nilai inlog
plt.imshow(img_inlog)#menampilkan gambar
plt.title("Inversi & Log")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_nthpower untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Mendefinisikan fungsi untuk nth power
def nthpower(c, y):#mendefinisikan sebuah fungsi Python yang bernama nthpower dengan satu parameter masukan c dan y
    thc = c / 100#mendefinisikan nilai thc
    thy = y / 100#mendefinisikan nilai thy
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = int(thc * pow(gray, thy))#perhitungan untuk menampilkan data nthpower
            if gray > 255:  # mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:  # mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_nthpower

#Menampilkan hasil
nthpower(50, 100)#mengatur nilai nth power
plt.imshow(img_nthpower)#menampilkan gambar
plt.title("Nth Power")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Membuat fungsi untuk nth root power
def nthrootpower(c, y):#mendefinisikan sebuah fungsi Python yang bernama nthrootpower dengan satu parameter masukan c dan y
    thc = c / 100#mendefinisikan nilai thc
    thy = y / 100#mendefinisikan nilai thy
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = int(thc * pow(gray, 1./thy))#perhitungan untuk menampilkan data nthrootpower
            if gray > 255:  # mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:  # mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_nthpower

#Menampilkan hasil
nthrootpower(50, 100)#mengatur nilai nthrootpower
plt.imshow(img_nthrootpower)#menampilkan gambar
plt.title("Nth Root Power")#membuat judul pada plot
plt.show()#menampilkan plot