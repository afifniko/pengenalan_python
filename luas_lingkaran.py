import math

def luas_setengah_lingkaran(jari_jari):
    luas = 0.5 * math.pi * (jari_jari ** 2)
    return luas

# Contoh penggunaan
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas = luas_setengah_lingkaran(jari_jari)
print(f"Luas setengah lingkaran dengan jari-jari {jari_jari} adalah: {luas}")
