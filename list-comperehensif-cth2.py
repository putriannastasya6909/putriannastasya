seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)
    
print(seq)

# penulisan list comperehensif
seq = [i * 2 for i in range(10) if i % 2 == 1]

print(seq)
