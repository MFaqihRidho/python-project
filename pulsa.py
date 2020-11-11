saldo = 1000000000000
lanjut_beli = 'y'
user = {'username':'test','password':'123456'}
logged = 'gagal'

def beli_pulsa(p):
    global saldo
    if saldo >= int(p):
        saldo -= int(p)
        print('Anda berhasil Membeli Pulsa',p)
        print('Sisa Saldo Anda Adalah Rp',saldo)
    else:
        print('Saldo Anda Tidak Mencukupi Silahkan Coba lagi')
        
while logged == 'gagal':
    print("Selamat datang di Pulsa Bank jago\nMau Beli pulsa? Login dulu")
    Username = input("Username: ")
    Password = input("Password: ")
    if str(Username) == user['username'] and Password == user['password']:
        print("Selamat Datang",user['username'])
        logged = 'berhasil'
    else:
        print('Username Atau Password salah Coba lagi')

while lanjut_beli == 'y' and logged == 'berhasil':
    print("1.Pulsa Rp5.000")
    print("2.Pulsa Rp10.000")
    print("3.Pulsa Rp25.000")
    print("4.Pulsa Rp50.000")
    print("5.Pulsa Rp100.000")
    print("6.Isi Sendiri")
    print("7.Keluar Aplikasi")
    pilih = int(input("Pilih Pulsa yang mau di beli: "))
    if pilih == 1:
        beli_pulsa(5000)
    elif pilih == 2:
        beli_pulsa(10000)
    elif pilih == 3:
        beli_pulsa(25000)
    elif pilih == 4:
        beli_pulsa(50000)
    elif pilih == 5:
        beli_pulsa(100000)
    elif pilih == 6:
        beli_pulsa(input("Masukan Nominal pulsa Rp:"))
    elif pilih == 7:
        lanjut_beli = 'n'
    else:
        print("Salah Masukan Nomor")
        lanjut_beli = input("Lanjut Beli? (y/n)").lower()



import time

def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
    print("Done!")
    

if __name__ == '__main__':
    countdownTimer(25, 00) #pomodoro timer










