# List comprehension dengan if-else
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ambil hanya angka genap
even = [n for n in numbers if n % 2 == 0]
print(even)

# Ubah angka menjadi kategori
categories = ["Genap" if n % 2 == 0 else "Ganjil" for n in numbers]
print(categories)
