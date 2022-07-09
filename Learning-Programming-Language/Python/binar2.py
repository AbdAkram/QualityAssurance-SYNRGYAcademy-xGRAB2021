# penggunaan continue pada while
bilangan = 0
pilihan = 'y'
 
while (pilihan != 'n'):
    bilangan = int(input("Masukkan bilangan di bawah 100: "))
     
    if (bilangan > 100):
        print("Bilangan melebihi angka 100. Coba lagi.")
        continue
         
    print("Pangkat dua dari bilangan ini adalah", bilangan*bilangan)
    pilihan = input("Apakah Anda ingin mengulangi lagi (y/n)?")
print("Baik Terima Kasih!")