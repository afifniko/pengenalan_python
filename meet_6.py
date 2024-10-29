# fungction
# set / kumpulan perintah
# algoritma :
# langkah - langkah / perintah untuk memecah masalah

# function di python
# function biasa
# function dengan input
# function dengan return\

#!function biasa

# def print_hello ():#! penulisan nama fungction -> huruf
#     print("hello sayang") 
# print_hello()

# def perkenalan():
#     print(127)
#     print("NIKO")
#     print("PRODI INFORMAITKA")
#     print("JOGJA")
# perkenalan()

# break,continue,pass
# def gabut():
#     pass

#!function dengan input(input = menerima value)

# def luas_persegi_panjang(panjang,lebar):
#     luas = panjang * lebar
#     print(luas)
#     print(f"luas persegi panjang dengan panjang {panjang} dan lebara {lebar} adalah {luas}")
# luas_persegi_panjang(7,4)

# def perkenalan(nama:str,asal:str,npm:int):
#     print(nama)
#     print(asal)
#     print(npm)

#     # print(f" nama saya {nama} asal saya dari {asal} dan nomor npm saya adalah{npm}")
# perkenalan("niko",127,"jogja")
# perkenalan(nama="niko", asal="jogja", npm=127)

# def luas_persegi_panjang():
#     print("menghitung  luas persegi panjang")
#     panjang = int(input("masukan panjang"))
#     lebar = int(input("masukan lebar"))
#     luas = panjang * lebar
#     print(luas)
#     print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
# luas_persegi_panjang()

#!fungction dengan return

# def luas_persegi_panjang(panjang,lebar):
#     luas = panjang * lebar
#     return luas 

# luas = luas_persegi_panjang(4,5)
# luas_baru = luas * 10
# luas_persegi_panjang()

# def hello():
#     return "hello sayang" 
# nilai = hello()
# print(hello()) #  == print("hello")

# def luas_segitiga(alas , tinggi): #parameter
#     # luas = (alas * tinggi) / 2
#     return (alas * tinggi) / 2
# luas = luas_segitiga(10,10)
# luas_segitiga_baru = luas_segitiga * 2
# print(luas_segitiga_baru)