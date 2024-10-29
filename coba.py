isContinue = input("menghitung luas apakah (persegi/segitiga)?")
if isContinue == "persegi":
    def input_user():
        LEBAR = int(input("masukkan nilai lebar :"))
        PANJANG = int(input("masukkan nilai panjang :"))

        return LEBAR,PANJANG

    def hitung_luas(LEBAR,PANJANG):
        return LEBAR*PANJANG

    def display(massage,value):
        print(f"hasil perhitungan {massage} = {value}")


    LEBAR,PANJANG = input_user()   
    LUAS = hitung_luas(LEBAR,PANJANG)

    display("luas PERSEGI",LUAS)

if isContinue == "segitiga":
    def input_user():
        ALAS = int(input("masukkan nilai alas :"))
        TINGGI = int(input("masukkan nilai tinggi :"))

        return ALAS,TINGGI

    def hitung_luas(ALAS,TINGGI):
        return 2*(ALAS+TINGGI)

    def display(massage,value):
        print(f"hasil perhitungan {massage} = {value}")


    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)

    display("luas SEGITIGA",LUAS)