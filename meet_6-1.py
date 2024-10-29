# ketika ada return dibuatkan var untuk di panggil
def header():
    print("="*5,"PROGRAM MENGHITUNG LUAS DAN KELILING","="*5)
    print("="*15,"PERSEGI PANJANG","="*15)


def input_user():
    panjang = int(input("Masukan Panjang"))
    lebar = int(input("Masukan lebar"))
    return panjang , lebar


def hitung_luas(panjang,lebar):
    return panjang * lebar


def hitung_keliling(panjang,lebar):
    return 2*(panjang + lebar)

def tampilkan_output(panjang,lebar,luas,kelilling):
    print(f"panjang\t :{panjang}")
    print(f"lebar\t :{lebar}")
    print(f"Luas\t :{luas}")
    print(f"Keliling :{keliling}")
    print("="*40)


# buat program berulang untuk menghitung luas & keliling
    header()
while True:
    panjang,lebar = input_user()
    luas = hitung_luas(panjang,lebar)
    keliling = hitung_keliling(panjang,lebar)
    tampilkan_output(panjang,lebar,luas,keliling)
    is_break = input("lanjutkan program (y/n) :")
    if is_break == "n":
        break