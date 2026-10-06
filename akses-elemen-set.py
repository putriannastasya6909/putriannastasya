fellowship = {'aragorn', 'gimli', 'legolas'}

for p in fellowship:
    print(p)
    
# Eliminasi elemen duplikat
# contoh 1
data = {1, 2, 3, 2, 1, 4, 5, 2, 3, 5}
print(data)
# output ➜ {1, 2, 3, 4, 5}

#contoh 2
data = [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
print(data)
# output ➜ [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]

data_unique_set = set(data)
print(data_unique_set)
# output ➜ {1, 2, 3, 4, 5}

data_unique = list(data_unique_set)
print(data_unique)
# output ➜ [1, 2, 3, 4, 5]
