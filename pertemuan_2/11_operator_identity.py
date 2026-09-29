# Identity operators: is, is not
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)  # True (sama object)
print(x is y)  # False (beda object)
print(x == y)  # True (nilai sama)
