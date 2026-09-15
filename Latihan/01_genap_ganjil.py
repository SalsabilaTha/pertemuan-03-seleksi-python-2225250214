# Input: satu bilangan bulat
# Proses: mengecek sisa pembagian dengan 2
# Output: bilangan genap atau ganjil

bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")