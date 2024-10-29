#operasi logika
# -and
# -or
# -not
# -xor '^' (nilai sama = false)

# operasi and (keduanya harus benar)
a = True
b = True
c = a and b
print (f'a ({a}) and b ({b}) = {c}')
a = True
b = False
c = a and b
print (f'a ({a}) and b ({b}) = {c}')
a = False
b = False
c = a and b
print (f'a ({a}) and b ({b}) = {c}')

#operasi or (minimal salah satu benar)
a = True
b = True
c = a or b
print(f'a {a} or {b} = {c}')
a = False
b = True
c = a or b
print(f'a {a} or {b} = {c}')
a = False
b = False
c = a or b
print(f'a {a} or {b} = {c}')

# not (negasi) (mengubah nilai awal)
a =  True
c = not a
print(f'negasi a {a}= {c}')

# xor ^ (gak boleh ada yang sama (kalo sama false))
a = True
b = True
c = a ^ b
print (f'a ({a}) xor b ({b}) = {c}')

a = True
b = False
c = a ^ b
print (f'a ({a}) xor b ({b}) = {c}')





