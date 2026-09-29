# Label untuk perulangan (menggunakan break dengan nested loop)
outer = True
while outer:
    for i in range(5):
        if i == 3:
            outer = False
            break
        print(i)
    if not outer:
        break

print("Selesai")

# Alternatif dengan fungsi
def labeled_loop():
    for i in range(3):
        for j in range(3):
            if j == 1:
                return
            print(f"({i}, {j})")

labeled_loop()
