import numpy as np#memanggil library numpy untuk mengolah array
import imageio#memanggil library imageio untuk mengolah array
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt

img = imageio.imread("sunset.jpg")#membaca gambar dengan nama sunset.jpg dan menyimpannya ke dalam variable image

img_height = img.shape[0] #membuat variable tinggi gambar dan menyimpannya ke dalam variable img_height
img_width = img.shape[1] #membuat variable lebar gambar dan menyimpannya ke dalam variable img_width
img_channel = img.shape[2] #membuat variable channel gambar dan menyimpannya ke dalam variable img_channel

img_grayscale = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
        green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
        blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
        gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
        img_grayscale[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_grayscale

plt.imshow(img_grayscale)#menampilkan gambar
plt.title("Grayscale")#membuat judul pada plot
plt.show()#menampilkan semua plot

#menampilkan histogram gambar grayscale
hg = np.zeros((256))#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    hg[x] = 0#menginisialisasikan nilai x ke 0
for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]#mengambil nilai piksel gray pada titik (y,x)
        hg[gray] += 1#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)#untuk membuat array yang memiliki nilai dari 0 hingga 256 dengan interval 100, yang kemudian digunakan sebagai bins untuk membagi data dalam histogram
plt.hist(hg, bins, color="black", alpha=0.5)#untuk menggambar histogram dengan warna hitam (color="black") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
plt.title("Histogram")#membuat judul pada plot
plt.show()#menampilkan semua plot

hgr = np.zeros((256))#membuat array Numpy pada variable hgr dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
hgg = np.zeros((256))#membuat array Numpy pada variable hgr dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
hgb = np.zeros((256))#membuat array Numpy pada variable hgr dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
hgrgb = np.zeros((768)) #membuat array Numpy pada variable hgr dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 768

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    hgr[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgr
    hgg[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgg
    hgb[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgb

for x in range(0, 768):#melakukan perulangan pada setiap piksel pada sumbu x
    hgrgb[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgrgb

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    hgr[x] = 0  # menginisialisasikan nilai x ke 0 pada variable hgr
    hgg[x] = 0  # menginisialisasikan nilai x ke 0 pada variable hgg
    hgb[x] = 0  # menginisialisasikan nilai x ke 0 pada variable hgb

for x in range(0, 768):#melakukan perulangan pada setiap piksel pada sumbu x
    hgrgb[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgrgb

# th = int(256/64)
temp = [0]#mengatur nilai temp ke 0
for y in range(0, img.shape[0]):#melakukan perulangan pada setiap piksel pada sumbu x untum img.shape
    for x in range(0, img.shape[1]):#melakukan perulangan pada setiap piksel pada sumbu y untum img.shape
        red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
        green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
        blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
        green = green + 256 #mengatur nilai green dengan menambahkan nilai 256
        blue = blue + 512 #mengatur nilai blue dengan menambahkan nilai 512
        #         temp.append(green)
        hgrgb[red] += 1#menambahkan nilai 1 setiap parameter red pada nilai rata-rata piksel
        hgrgb[green] += 1#menambahkan nilai 1 setiap parameter green pada nilai rata-rata piksel
        hgrgb[blue] += 1#menambahkan nilai 1 setiap parameter blue pada nilai rata-rata piksel

binsrgb = np.linspace(0, 768, 100)#untuk membuat array yang memiliki nilai dari 0 hingga 768 dengan interval 100, yang kemudian digunakan sebagai bins untuk membagi data dalam histogram
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)#untuk menggambar histogram dengan warna hitam (color="black") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")#membuat judul pada plot
plt.show()#menampilkan semua plot

for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
        green = img[y][x][1]  # mengambil nilai piksel green pada titik (y,x)
        blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
        hgr[red] += 1#menambahkan nilai 1 setiap parameter hgr pada nilai rata-rata piksel
        hgg[green] += 1#menambahkan nilai 1 setiap parameter hgg pada nilai rata-rata piksel
        hgb[blue] += 1#menambahkan nilai 1 setiap parameter hgb pada nilai rata-rata piksel

bins = np.linspace(0, 256, 100)#untuk membuat array yang memiliki nilai dari 0 hingga 256 dengan interval 100, yang kemudian digunakan sebagai bins untuk membagi data dalam histogram
plt.hist(hgr, bins, color="red", alpha=0.5)#untuk menggambar histogram dengan warna merah (color="red") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
plt.title("Histogram Red")#membuat judul pada plot
plt.show()#menampilkan semua plot

plt.hist(hgg, bins, color="green", alpha=0.5)#untuk menggambar histogram dengan warna hijau (color="green") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
plt.title("Histogram Green")#membuat judul pada plot
plt.show()#menampilkan semua plot

plt.hist(hgb, bins, color="blue", alpha=0.5)#untuk menggambar histogram dengan warna hijau (color="green") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
plt.title("Histogram Blue")#membuat judul pada plot
plt.show()#menampilkan semua plot

hgk = np.zeros((256))#membuat array Numpy pada variable hgk dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
c = np.zeros((256))#membuat array Numpy pada variable c dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    hgk[x] = 0 #menginisialisasikan nilai x ke 0 pada variable hgk
    c[x] = 0# menginisialisasikan nilai x ke 0 pada variable c

for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]  # mengambil nilai piksel gray pada titik (y,x)
        hgk[gray] += 1# menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel

c[0] = hgk[0]#mengatur nilai c sama dengan hgk
for x in range(1, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    c[x] = c[x - 1] + hgk[x]#rumus dari perulangan dengan menambahkan nilai hgk

hmaxk = c[255]#mengatur nilai hmaxk samadengan c[255]

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    c[x] = 190 * c[x] / hmaxk#rumus dari perulangan dengan membagi nilai hgk

plt.hist(c, bins, color="black", alpha=0.5)#untuk menggambar histogram dengan warna hitam (color="hitam") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
plt.title("Histogram Grayscale Kumulatif")#membuat judul pada plot
plt.show()#menampilkan semua plot

hgh = np.zeros((256))#membuat array Numpy pada variable hgh dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
h = np.zeros((256))#membuat array Numpy pada variable h dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
c = np.zeros((256))#membuat array Numpy pada variable c dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    hgh[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgh
    h[x] = 0#menginisialisasikan nilai x ke 0 pada variable h
    c[x] = 0#menginisialisasikan nilai x ke 0 pada variable c

for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]  # mengambil nilai piksel gray pada titik (y,x)
        hgh[gray] += 1 #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel

h[0] = hgh[0] #mengatur nilai h samadengan hgh
for x in range(1, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    h[x] = h[x - 1] + hgh[x]#rumus dari perulangan dengan menambahkan nilai hgh

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    h[x] = h[x] / img_height / img_width#rumus dari perulangan dengan membagi img_height dengan img_width

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    hgh[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgh

for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]  # mengambil nilai piksel gray pada titik (y,x)
        gray = h[gray] * 255#perhitungan mengalikan nilai h dengan 255
        hgh[int(gray)] += 1 #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel

c[0] = hgh[0]#mengatur nilai h sama dengan hgh
for x in range(1, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    c[x] = c[x - 1] + hgh[x]#perhitungan untuk perulangan

hmaxk = c[255]#mengatur nilai hmaxk samadengan c[255]

for x in range(0, 256):#melakukan perulangan pada setiap piksel pada sumbu x
    c[x] = 190 * c[x] / hmaxk#perhitungan untuk perulangan

plt.hist(c, bins, color="black", alpha=0.5)#untuk menggambar histogram dengan warna hitam (color="hitam") dan transparans
plt.title("Histogram Grayscale Hequalisasi")#membuat judul pada plot
plt.show()#menampilkan semua plot