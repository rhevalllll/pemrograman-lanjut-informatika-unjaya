def awal(*args):
    print("Toko Buah Koperasi UNJANI Yogyakarta")
    jumlah_buah = int(input("Masukan Banyaknya Buah Yang Dibeli : "))

    for i in range(jumlah_buah):
        buah = input(f"buah {i+1} : ")
        args+= (buah,)

        print("buah yang anda beli adalah : ")
        for i, buah in enumerate (args):
            print(f"{i+1}. {buah}")
    print("terimakasih")
awal()