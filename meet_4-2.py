# Program Konversi Nilai

nilai = float(input('berikan nilai kamu'))
A = nilai >= 81 
B = 61 >= nilai <81
C = 41 >= nilai < 61
D = 21 >= nilai < 41
E = nilai < 21

if nilai >= 81 :
    print('Nilai anda adalah A')
elif nilai >= 61:
    print("Nilai anda adalah B")
elif nilai >= 41:
    print("Nilai anda adalah C")
elif nilai >= 21:
    print("Nilai anda adalah D")
else :
    print("Nilai anda adalah E")
