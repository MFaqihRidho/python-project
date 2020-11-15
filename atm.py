pin = "12345"
saldo = 100

def StartAtm():
    print("Tekan 1 untuk memasukan Kartu")
    CardIn = input("Masukan Kartu Atm Anda : ")
    if CardIn == "1":
        print("kamu berhasil memasukan kartu")
        def StartPin():
            Pinin = input("Masukan pin Anda: ")
            if Pinin == pin:
                print("pin yang Anda Masukan Benar")
                def StartChoice():
                    choice = input("1.Tarik Saldo\n2.Cek saldo\n")
                    if choice == "1":
                        choice2 = input("1.Rp100.000 2.Rp1.000.000\n")
                        x = 100000
                        y = 1000000
                        if choice2 == "1":
                            global saldo
                            if saldo > x:
                                saldo = saldo - x
                                print("penarikan Berhasil sisa saldo Anda: ",saldo)
                            else:
                                print("Saldo Anda Tidak Mencukupi Untuk penarikan\n")
                        elif choice2 == "2":
                            if saldo > y:
                                saldo = saldo - y
                                print("penarikan Berhasil sisa saldo Anda: ",saldo)
                            else:
                                print("Maaf saldo anda Tidak Mencukupi Untuk Penarikan\n")
                                StartChoice()
                    elif choice == "2":
                        print("Sisa saldo anda",saldo)
                    else:
                        print("Angka yang anda masukan salah")
                        StartPin()
                StartChoice()
            else:
                print("Pin yang Anda masukan salah")
                StartPin()    
        StartPin()
    else:
        print("kartu Gagal Masuk")
        StartAtm()


StartAtm()



# pin = 12345
# saldo = 1000000
# saldo2 = 100000

# def Start_Atm():
#     print("Tekan 1 Untuk Memasukan Kartu")
#     kartu = int(input("Masukan Kartu Atm Anda: "))
#     if kartu == 1 :
#         print("\nKartu Berhasil Masuk")
#         def Start_Pin():
#             Pin_in = int(input("Masukan Pin Anda: "))
#             wrong_pin = 0
#             user_has_not_entered_correct_pin = true
#             wrong_pin = 3
#             while wrong_pin > 0 and user_has_not_entered_correct_pin:
#                 return pin
#             if pin_is_not_correct(pin):
#                 retries = retries - 1
#             else:
#                 user_has_not_entered_correct_pin = false
#             break
#             if Pin_in == pin:
#                 print("Pin Anda yang Masukan Benar")
#                 # def Start_Choice():
#                 #     print("Pilih Jenis Tranksaksi")
#                 #     Choice = input("\n1.Penarikan\n2.Transfer\n3.Pembelian\n4.Info Saldo\n5.Pembayaran\n6.Ubah Pin")
#                 #     if Choice == 1
#                 #     elif Choice == 2
#                 #     elif Choice == 3
#                 #     elif Choice == 4
#                 #     elif Choice == 5
#                 #     elif Choice == 6
#                 #     else
#                 # Start_Choice()
#             elif wrong_pin == 3:
#                 print("Pin anda sudah 3 kali salah Kartu tidak bisa diambil")
#             else:
#                 wrong_pin = wrong_pin + 1
#                 print("Pin yang Anda Masukan Salah")
#                 Start_Pin()
#         Start_Pin()
#     else:
#         print("Kartu Anda Gagal masuk Coba Lagi")
#         coba_lagi = input("Tekan 1 Untuk Coba Lagi: ")
#         if coba_lagi == '1':
#             Start_Atm()

# Start_Atm()



