# Nested operator logika
score = 75
attendance = 80

if (score >= 60 and attendance >= 75) or score >= 85:
    print("Lulus")
else:
    print("Tidak Lulus")

# Contoh kompleks
age = 20
has_license = True
is_healthy = True

if (age >= 18 and has_license) and not is_healthy:
    print("Bisa mengemudi tapi harus istirahat")
elif age >= 18 and has_license and is_healthy:
    print("Bisa mengemudi dengan sehat")
else:
    print("Tidak bisa mengemudi")
