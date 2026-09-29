# Iterasi pada dictionary
dict1 = {"name": "John", "age": 25, "city": "Jakarta"}

for key in dict1:
    print(f"{key}: {dict1[key]}")

print("---")

for key, value in dict1.items():
    print(f"{key}: {value}")
