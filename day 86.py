#MENENTUKAN BILANGAN POSITIF/NEGATIF

angka = int(input("Masukkan Angka : "))

if  angka > 0:
    print(f"{angka} adalah bilangan Positif")
elif angka == 0: 
    print("Bilangan 0")
else:
    print(f"{angka} adalah Bilangan Negatif")