# via method append()
list_1 =[10, 70, 20, 70]

list_1.append(88)
list_1.append(97)
print('after: ', list_1)

# via slicing
list_1 = [10, 70, 20] 
print('before: ', list_1) 

list_1[len(list_1):] = [88, 87] 
print('after: ', list_1)