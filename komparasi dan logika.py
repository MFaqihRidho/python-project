#komparasi dan juga logika

#-----4++++++++11--------

inputuser = float(input("masukan angka yang \n lebih dari 4 \n dan kurang dari 11: "))

#-----4++++++
islebihdari = (inputuser > 4)
print("lebih dari 4 adalah",islebihdari) 

#++++++11-----
iskurangdari = (inputuser < 11)
print("kurang dari 11 adalah  :",iskurangdari)


#-----4++++++++11--------
iscorrect = islebihdari and iskurangdari
print("angka yang anda masukan =",iscorrect)

print("\n",22*"=","\n")

#++++++4--------11+++++++

inputuser = float(input("masukan angka yang \n kurang dari 4 \n atau lebih dari 11: "))

#++++++4------
iskurangdari = (inputuser < 4)
print("kurang dari 4 adalah",iskurangdari) 

#______11++++++
islebihdari = (inputuser > 11)
print("lebih dari 11 adalah  :",islebihdari)

#-----4++++++++11--------
iscorrect = iskurangdari or islebihdari
print("angka yang anda masukan =",iscorrect)

print("\n",22*"=","\n")

#---------4++++++++10--------15++++++++20--------

inputuser = float(input("masukan angka yang \n lebih dari 4 dan kurang dari 10 \n atau lebih dari 15 dan kurang dari 20 : "))

#4+++++++
lebih4 = (inputuser > 4)
print("lebih dari 4 :",lebih4)

#++++++++10
kurang10 = (inputuser < 10)
print("kurang dari 10 :",kurang10)

#4+++++++10
lebih4kurang10 = lebih4 and kurang10

#15+++++++
lebih15 = (inputuser > 15)
print("lebih dari 15 :",lebih15)

#+++++++++20
kurang20 = (inputuser < 20)
print("kurang dari 20 :",kurang20)

#15++++++++20
lebih15kurang20 = lebih15 and kurang20

#---------4++++++++10--------15++++++++20--------
lebih4kurang10lebih15kurang20 = lebih4kurang10 or lebih15kurang20
print("Angka yang anda masukan :",lebih4kurang10lebih15kurang20)

print("\n",22*"=","\n")

#+++++++++0---------10+++++++++20---------30++++++++++

inputuser = float(input("masukan angka yang \n kurang dari 0 \n atau lebih dari 10 dan kurang dari 20 \n atau lebih dari 30 : "))

#++++++++0
kurangdari0 = (inputuser < 0)
print("kurang dari 0 : ",kurangdari0)

#10+++++++++++
lebihdari10 = (inputuser > 10)
print("lebih dari 10 : ",lebihdari10)

#+++++++++++20
kurangdari20 = (inputuser < 20)
print("kurang dari 20 : ",kurangdari20)

#10++++++++++20
lebihdari10kurangdari20 = lebihdari10 and kurangdari20
print("lebih dari 10 dan kurang dari 20 : ",lebihdari10kurangdari20)

#30++++++++++
lebihdari30 = (inputuser > 30)
print("Lebih dari 30 : ",lebihdari30)

#+++++++++0---------10+++++++++20---------30++++++++++
kurangdari0lebihdari10kurangdari20 = kurangdari0 or lebihdari10kurangdari20
kurangdari0lebihdari10kurangdari20lebihdari30 = kurangdari0lebihdari10kurangdari20 or lebihdari30

print("angka yang anda masukan : ",kurangdari0lebihdari10kurangdari20lebihdari30)