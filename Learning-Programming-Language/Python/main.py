#Angka Paling Besar
a = int(input("Masukkan a : "))
b = int(input("Masukkan b : "))
c = int(input("Masukkan c : "))

if a > b and a > c:
  print('A yang terbesar')
elif b > a and b > c:
  print('B yang terbesar')
else:
  print('C yang terbesar')

print(20*"=")

#Mengurutkan angka
a = int(input("Masukkan a : "))
b = int(input("Masukkan b : "))
c = int(input("Masukkan c : "))

d = [a, b, c]
d.sort()

print(d)

print(20*"=")

#angka ganjil/genap
a = int(input("Masukkan angka : "))

if (a % 2 == 1):
    print("Angka berikut adalah ganjil")
else:
    print("angka genap")

print(20*"=")

#Perpangkatan
a = int(input("Masukkan angka pertama(a) : "))
b = int(input("Masukkan angka kedua(b) : "))

c = a ** b

print("(a) pangkat (b) adalah : ", c)