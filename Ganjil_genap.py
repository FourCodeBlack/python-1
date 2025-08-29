bilangan = int(input("Masukkan bilangan : "))


#Ganjil genap

if bilangan > 0 :
    if bilangan == 1 :
     print("Bilangan ganjil")
    elif (bilangan % 2) == 0 :
     print(f"Hasil:{bilangan}adalah Bilangan genap")
    else:
     print("Bilagan ganjil")
else:
    print("APALAH")



# #Penjumlahan sampai bilangan tertentu

a = 0
b = 1

while b <= bilangan:
    a = a + b
    b+=1
print(a)



# Tabel perkiraan
k = 1

while k <= 10:
 hasil = bilangan *  k
 print(f"{bilangan} x {k} ={hasil} ")
 k+=1
    