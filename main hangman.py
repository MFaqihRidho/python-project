import random
from hangman import parts
from time import sleep



kata = ["anjing","kupu-kupu","kucing","manusia","kura-kura "]
terpilih = random.choice(kata)

benar = ['_'] * len(terpilih)
salah = []

def update():
  for i in benar:
    print(i,end = ' ')
  print()

print("Tunggu aku sedang memilih katanya...")

def wait():
    for i in range(1,6):
        print(".",end='')
        sleep(.5)
    print()

wait()

print("katanya memiliki panjang: ",len(terpilih),"huruf")

update()
parts(len(salah))

while True:
  print("\n=========================\n")

  tebak = input("Tebak katanya: ")
  print("kita cek")
  wait()

  if tebak in terpilih:
    index = 0
    for i in terpilih:
      if i == tebak:
        benar[index] = tebak
      index += 1
    update()


  else:
    if tebak not in salah:
      salah.append(tebak)
      parts(len(salah))
    else:
      print("kamu udah nebak")
    print(salah)
  
  if len(salah) > 4:
    print("kamu kalah")
    print("katanya adalah:",terpilih)
    break
  
  if "_" not in benar:
    print("Kamu menang")
    break