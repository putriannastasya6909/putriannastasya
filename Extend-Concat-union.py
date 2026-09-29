# via method extend()
list_1 = [10, 70, 20] 
list_2 = [88, 77] 
list_1.extend(list_2) 
print(list_1)

# via slicing
list_1 = [10, 70, 20] 
list_2 = [88, 77] 
list_1[len(list_1):] = list_2 
print(list_1)

# via operator +
list_1 = [10, 70, 20] 
list_2 = [88, 77] 
list_3 = list_1 + list_2 
print(list_3)