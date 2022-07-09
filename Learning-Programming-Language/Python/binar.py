#I/O
nama = input("siapa nama kamu ? ")
umur = input("berapa umur kamu ? ")
print("Hallo", nama, "umur kamu adalah", umur, "tahun")

job = input("lalu apa pekerjaan kamu sekarang ? ")
print("Waahh keren, pekerjaan kamu adalah", job)
print("-------------------------------------")

#Basic
buah = "durian"
sayur = "bayam"
print("buah yang saya suka adalah {} dan sayur yang saya suka {}" .format(buah, sayur)) #penulisan format
print("-------------------------------------")

#belajar angka
a = 2
print(a,a,a,a, sep="b", end="c")
print()
print("-------------------------------------")

#Coba Import
import math
print(math.pi)
print("-------------------------------------")

#matematika
a = input("a = ")
b = input("b = ")

print("Penjumlahan = ", float(a) + float(b))
print("Pengurangan = ", float(a) - float(b))
print("Perkalian = ", float(a) * float(b))
print("Pembagian = ", float(a) / float(b))