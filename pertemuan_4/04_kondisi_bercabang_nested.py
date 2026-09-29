# Nested If-Else
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Anda boleh mengemudi")
    else:
        print("Anda harus memiliki SIM")
else:
    print("Anda terlalu muda untuk mengemudi")

# Contoh lain
value = 50

if value > 100:
    print("Lebih dari 100")
else:
    if value > 50:
        print("Lebih dari 50 tapi kurang dari 100")
    elif value == 50:
        print("Sama dengan 50")
    else:
        print("Kurang dari 50")
