import numpy as np#memanggil library numpy untuk mengolah array
import cv2 #memanggil library cv2 untuk mengolah gambar
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt
img = cv2.imread('gunung.jpg')#membaca gambar dengan nama gunung.jpg dan menyimpannya ke dalam variable img

#define reso dan tipe gambar
img_height = img.shape[0] #membuat variable tinggi gambar dan menyimpannya ke dalam variable img_height
img_width = img.shape[1] #membuat variable lebar gambar dan menyimpannya ke dalam variable img_width
img_channel = img.shape[2] #membuat variable channel gambar dan menyimpannya ke dalam variable img_channel
img_type = img.dtype #membuat variable tipe gambar dan menyimpannya ke dalam variable img_type

#Percobaan pertama kita buat brightness untuk gambar gray scale

img_brightness = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#membuat fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai) :#mendefinisikan sebuah fungsi Python yang bernama brighter dengan satu parameter masukan nilai
    for y in range(0, img_height):#melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]#mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]#mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]#mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red)+int(green)+int(blue))/3#menghitung rata-rata nilai piksel pada titik (y,x)
            gray += nilai #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if gray > 255:#jika nilai gray lebih besar dari 255 maka nilai gray diset menjadi 255
                gray = 255
            if gray < 0:# jika nilai gray kurang dari 0 maka nilai gray diset menjadi 0
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_brightness

fig, axes = plt.subplots(ncols=2)#membuat plot dengan dua kolom
ax = axes.ravel()#menyusun plot ke dalam bentuk array
brighter(-100)#mengatur fungsi brighter dengan parameter -100
ax[0].imshow(img_brightness)#menampilkan gambar
ax[0].set_title("Brighness -100")#memberikan judul pada plot
brighter(50)#mengatur fungsi brighter dengan parameter 50
ax[1].imshow(img_brightness)#menampilkan gambar
ax[1].set_title("Brighness 50")#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

#brightness RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai):#mendefinisikan sebuah fungsi Python yang bernama brighter dengan satu parameter masukan nilai
    for y in range(0, img_height):#melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]#mengambil nilai piksel red pada titik (y,x)
            red += nilai#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if red > 255:#jika nilai red lebih besar dari 255 maka nilai red diset menjadi 255
                red = 255
            if red < 0:#jika nilai red kurang dari dari 0 maka nilai red diset menjadi 0
                red = 0
            green = img[y][x][1]#mengambil nilai piksel green pada titik (y,x)
            green += nilai#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if green > 255:#jika nilai green lebih besar dari 255 maka nilai green diset menjadi 255
                green = 255
            if green < 0:#jika nilai green kurang dari dari 0 maka nilai green diset menjadi 0
                green = 0
            blue = img[y][x][2]#mengambil nilai piksel blue pada titik (y,x)
            blue += nilai#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if blue > 255:#jika nilai blue lebih besar dari 255 maka nilai blue diset menjadi 255
                blue = 255
            if blue < 0:#jika nilai blue kurang dari dari 0 maka nilai blue diset menjadi 0
                blue = 0
            img_brightness[y][x] = (red, green, blue)#menyimpan nilai piksel red, green, blue yang sudah diatur sebelumnya pada variabel img_brightness
fig, axes = plt.subplots(ncols=2)#membuat plot dengan dua kolom
ax = axes.ravel()#menyusun plot ke dalam bentuk array
rgbbrighter(-100)#mengatur fungsi rgbbrighter dengan parameter -100
ax[0].imshow(img_brightness)#menampilkan gambar
ax[0].set_title("Brighness -100")#memberikan judul pada plot
rgbbrighter(100)#mengatur fungsi rgbbrighter dengan parameter 100
ax[1].imshow(img_brightness)#menampilkan gambar
ax[1].set_title("Brighness 100")#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

#contrast
img_contrass = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

def contrass(nilai):#mendefinisikan sebuah fungsi Python yang bernama brighter dengan satu parameter masukan nilai
    for y in range(0, img_height):#melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  #mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  #mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  #mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  #menghitung rata-rata nilai piksel pada titik (y,x)
            gray += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if gray > 255:  #jika nilai gray lebih besar dari 255 maka nilai gray diset menjadi 255
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_contrass

fig, axes = plt.subplots(ncols=2)#membuat plot dengan dua kolom
ax = axes.ravel()#menyusun plot ke dalam bentuk array
contrass(50)#mengatur fungsi contrass dengan parameter 50
ax[0].imshow(img_contrass)#menampilkan gambar
ax[0].set_title("Contrass 50")#memberikan judul pada plot
contrass(100)#mengatur fungsi contrass dengan parameter 100
ax[1].imshow(img_contrass)#menampilkan gambar
ax[1].set_title("Contrass 100")#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua subplot


#Brightness Contrass RGB
img_rgbcontrass = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbcontrass(nilai):#mendefinisikan sebuah fungsi Python yang bernama brighter dengan satu parameter masukan nilai
    for y in range(0, img_height):#melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  #mengambil nilai piksel red pada titik (y,x)
            red += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if red > 255:  #jika nilai red lebih besar dari 255 maka nilai red diset menjadi 255
                red = 255
            green = img[y][x][1]  #mengambil nilai piksel green pada titik (y,x)
            green += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if green > 255:  #jika nilai green lebih besar dari 255 maka nilai green diset menjadi 255
                green = 255
            blue = img[y][x][2]  #mengambil nilai piksel blue pada titik (y,x)
            blue += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if blue > 255:  #jika nilai blue lebih besar dari 255 maka nilai blue diset menjadi 255
                blue = 255
            img_rgbcontrass[y][x] = (red, green, blue)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_rgbcontrass
fig, axes = plt.subplots(ncols=2)#membuat plot dengan dua kolom
ax = axes.ravel()#menyusun plot ke dalam bentuk array
rgbcontrass(50)#mengatur fungsi rgbcontrass dengan parameter 50
ax[0].imshow(img_rgbcontrass)#menampilkan gambar
ax[0].set_title("Contrass 50")#memberikan judul pada plot
rgbcontrass(100)#mengatur fungsi rgbcontrass dengan parameter 100
ax[1].imshow(img_rgbcontrass)#menampilkan gambar
ax[1].set_title("Contrass 100")#memberikan judul pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua subplot

#Contrass Auto Level
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

def autocontrass():#mendefinisikan sebuah fungsi Python yang bernama brighter
    #Inisialisasi variabel xmax, xmin, dan d dengan nilai awal.
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):  #melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  #melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  #mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # engambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  #mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  #menghitung rata-rata nilai piksel pada titik (y,x)
            if gray < xmax:#jika nilai gray lebih besar dari xmax maka nilai gray diset menjadi xmax
                xmax = gray
            if gray > xmin:#jika nilai gray lebih besar dari xmin maka nilai gray diset menjadi xmin
                xmin = gray
    d = xmin-xmax #mengurangkan parameter xmin dengan xmax
    for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
        for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # engambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = int(float(255/d) * (gray-xmax))#melakukan perhitungan di setiap parameter untuk mendapatkan hasil desimal
            img_autocontrass[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_autocontrass
autocontrass()#Memanggil fungsi autocontrass() untuk mengaplikasikan proses "auto level" pada gambar.
plt.imshow(img_autocontrass)#menampilkan gambar
plt.title("Contrass Autolevel")#membuat judul pada plot
plt.show()#menampilkan semua plot
