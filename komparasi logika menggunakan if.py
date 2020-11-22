#-----4++++++++11--------
x = float(input("Masukkan angka yang lebih dari 4 \ndan kurang dari 11 : "))
if  x > 4 and x < 11:
    print("Angka yang anda Masukan",True)
else :
	print("Angka yang anda Masukan",False)

print("\n","="*10,"\n")

#++++++4--------11+++++++
x = float(input("Masukkan angka yang kurang dari 4 \natau lebih dari 11 : "))
if  x < 4 or x > 11:
    print("Angka yang anda Masukan",True)
else :
	print("Angka yang anda Masukan",False)

print("\n","="*10,"\n")

#---------4++++++++10--------15++++++++20--------
x = float(input("Masukkan angka yang lebih dari 4 dan kurang dari 10 \natau lebih dari 15 dan kurang dari 20 : "))
if  (x > 4 or x < 10) or (x > 15 and x < 20):
    print("Angka yang anda Masukan",True)
else :
	print("Angka yang anda Masukan",False)

print("\n","="*10,"\n")

#+++++++++0---------10+++++++++20---------30++++++++++

x = float(input("Masukkan angka yang kurang dari 0 \natau lebih dari 10 dan kurang dari 20 \natau lebih dari 30 : "))
if  (x < 0) or (x > 10 and x < 20) or (x > 30):
    print("Angka yang anda Masukan",True)
else :
	print("Angka yang anda Masukan",False)


