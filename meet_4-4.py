# kalkulator sederhana

print('='*32)
print('-'*5,'Kalkulator sederhana')
print('='*32)
print("\n")
nilai_1 = float(input('Inputkan Angka Pertama :'))
nilai_2 = float(input('Inputkan Angka Kedua :'))
operator = input('Inputkan Operator (+,-,/,*,**,//,%):')

# penjumlahan
if operator == '+':
    hasil = nilai_1 + nilai_2
    print(f'hasil {nilai_1} + {nilai_2} ={hasil}')
# pengurangan
if operator == '-':
    hasil = nilai_1 - nilai_2
    print(f'hasil {nilai_1} - {nilai_2} ={hasil}')
# perkalian
if operator == '*':
    hasil = nilai_1 * nilai_2
    print(f'hasil {nilai_1} * {nilai_2} ={hasil}')
# pembagian
if operator == '/':
    hasil = nilai_1 / nilai_2
    print(f'hasil {nilai_1} / {nilai_2} ={hasil}')
# pangkat
if operator == '**':
    hasil = nilai_1 ** nilai_2
    print(f'hasil {nilai_1} ** {nilai_2} ={hasil}')
# modulus
if operator == '%':
    hasil = nilai_1 % nilai_2
    print(f'hasil {nilai_1} % {nilai_2} ={hasil}')
# floor div
if operator == '//':
    hasil = nilai_1 // nilai_2
    print(f'hasil {nilai_1} // {nilai_2} ={hasil}')
else :
    print('Operator tidak sesuai')

print('='*32)