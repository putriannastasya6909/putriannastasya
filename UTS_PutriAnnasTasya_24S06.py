nama = input("Masukkan nama mahasisswa: ")
nilai = float(input("Masukkan nilai mahasiswa: ")
              
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai>=85:
    print("Nama:", nama")
    print("Status: Lulus")
    print("Predikat: A")
elif nilai>=75:
    print("Nama:", nama")
    print("Status: Lulus")
    print("Predikat: B")
elif nilai>=60:
    print("Nama:", nama")
    print("Status: Lulus")
    print("Predikat: C")
else:
    print("Nama:", nama")
    print("Status: Tidak Lulus")
    print("Predikat: D")

print("-----------------------------------------------------------")

for angka in range (1, 21):
    if angka % 2 !=0:
        print(angka)
        
print("-----------------------------------------------------------")

angka = 0
while angka < 10:
    angka+=1
    
    if angka%2==0:
        continue
        
    print(angka)_
    
print("-----------------------------------------------------------")

buah = ["Apel", "Jeruk", "Mangga"]
buah.append("Pisang")
buah[0] = "Anggur"

print(buah)
