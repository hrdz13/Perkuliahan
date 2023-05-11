import numpy as np#memanggil library numpy untuk mengolah array
import imageio#memanggil library imageio untuk mengolah array
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt

img = imageio.imread("sunset.jpg")#membaca gambar dengan nama sunset.jpg dan menyimpannya ke dalam variable image

img_height = img.shape[0] #membuat variable tinggi gambar dan menyimpannya ke dalam variable img_height
img_width = img.shape[1] #membuat variable lebar gambar dan menyimpannya ke dalam variable img_width
img_channel = img.shape[2] #membuat variable channel gambar dan menyimpannya ke dalam variable img_channel
img_type = img.dtype #membuat variable tipe gambar dan menyimpannya ke dalam variable img_type

img_flip_horizontal = np.zeros(img.shape, img_type)#fungsi untuk mengatur nilai ke 0 lalu disimpan pada variable img_flip_horizontal
img_flip_vertical = np.zeros(img.shape, img_type) #fungsi untuk mengatur nilai ke 0 lalu disimpan pada variable img_flip_vertical

#Membalik gambar secara horizontal
for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        for c in range(0, img_channel):# melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_channel
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]#fungsi untuk membuat gambar menjadi terbalik secara horizontal

#Membalik gambar secara vertical
for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        for c in range(0,img_channel):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_channel
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]#fungsi untuk membuat gambar menjadi terbalik secara vertikal

#Menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal)#menampilkan gambar
plt.title("Flip Horizontal")#membuat judul pada plot
plt.show()#menampilkan plot
plt.imshow(img_flip_vertical)#menampilkan gambar
plt.title("Flip Vertical")#membuat judul pada plot
plt.show()#menampilkan plot