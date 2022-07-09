#function
def function(a, b):
    print(a ** b)
    print(a // b)
    print(a == b)

function(10, 5)

def mahasiswa(nama, nim):
    print("Nama Mahasiswa:", nama)
    print("NIM:", nim)

mahasiswa("Abdullah Akram",193015125)

#Arbitrary Argumen
def function2(*buah):
    print("Buah paling enak adalah:", buah[2])

function2("mangga","alpukat","durian","apel","melon")