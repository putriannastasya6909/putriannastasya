# Ternary operator untuk menentukan nilai
x = 10
y = 20

max_value = x if x > y else y
print(f"Nilai terbesar: {max_value}")

# Nested ternary
value = 45
category = "Tinggi" if value >= 80 else ("Sedang" if value >= 50 else "Rendah")
print(category)
