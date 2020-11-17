# class hero():
#     jumlah = 0
#     nama_hero = ''
#     def __init__(self,inputname,inputpower,inputhealth,inputarmor):
#         self.name = inputname
#         self.power = inputpower
#         self.health = inputhealth
#         self.armor = inputarmor
#         hero.jumlah += 1
#         hero.nama_hero += inputname + ','
#         #Private variable Memakai Double underscore
#         self.__Private = 'Private'
#         #Protected Variable Memakai single underscore
#         self._Protected = 'protect'

#     def sayname(self):
#         print("Namaku Adalah " + self.name)

#     def healthup(self,up):
#         self.health += up

#     def attack(self,opponent):
#         print(self.name + " Menyerang " + opponent.name)
#         opponent.defense(self,self.power)

#     def defense(self,opponent,attack_power):
#         print(self.name + " diserang " + opponent.name)
#         receive_attack = attack_power / self.armor
#         print("serangan Terasa: " + str(receive_attack))
#         self.health -= receive_attack
#         print("Darah " + self.name + " Tersisa: " + str(self.health))




# zilong = hero("Zilong",100,100,50)
# alucard = hero("alucard",150,50,50)
# ucup = hero("ucup",1000,1000,1)

# # zilong.attack(ucup)


# # while ucup.health > 0:
# #     zilong.attack(ucup)
# #     print("\n")

# zilong._Protected == 'test'
# print(zilong._Protected)
# print(zilong.__dict__)

# class hero():
#     __jumlah = 0
#     def __init__(self,inputname,inputpower,inputhealth,inputarmor):
#         self.__name = inputname
#         self.__power = inputpower
#         self.__health = inputhealth
#         self.__armor = inputarmor
#         hero.__jumlah += 1

#     def getname(self):
#         return self.__name

#     def getpower(self):
#         return self.__power

#     def uppower(self,up):
#         self.__power += up

#     #Hanya untuk Object
#     def getjumlah(self):
#         return hero.__jumlah

#     #Hanya untuk class
#     def getjumlah1():
#         return hero.__jumlah

#     #Nempel ke objek dan juga class
#     @staticmethod
#     def getjumlah2():
#         return hero.__jumlah

#     #Bisa Objek dan class juga tapi bisa tambah argumen
#     @classmethod
#     def getjumlah3(chara):
#         return chara.__jumlah


# zilong = hero("zilong",100,100,100)
# print(zilong.getjumlah())
# alucard = hero("alucard",100,100,100)
# print(hero.getjumlah1())
# miya = hero("miya",100,100,100)
# print(miya.getjumlah2())
# argus = hero("argus",100,100,100)
# print(hero.getjumlah3())

# class hero():
#     def __init__(self,inputname,inputpower):
#         self.name = inputname
#         self.__power = inputpower

#     @property
#     def info(self):
#         return "name {} : \npower : {}".format(self.name,self.__power)

#     @property
#     def power(self):
#         pass

#     @property.getter
#     def power(self):
#         return self.__power

#     @property.setter
#     def power(self,input):
#         self.__power = input

#     @property.deleter
#     def power(self):
#         print("armor has deleted")
#         self.__power = none


# zilong = hero("zilong",100)

# print("merubah info")
# print(zilong.info)
# zilong.name = "ucup"
# print(zilong.info)


# class Hero():
#     __jumlah = 0
#     def __init__(self,name,health,power,defense):
#         self.__name = name
#         self.__healthStandar = health
#         self.__powerStandar = power
#         self.__defenseStandar = defense
#         self.__level = 1
#         self.__exp = 0
        
#         self.__healthMax = (self.__healthStandar * self.__level)
       
#         self.__power = self.__powerStandar * self.__level
#         self.__defense = self.__defenseStandar * self.__level
#         self.__health = self.__healthMax
#         Hero.__jumlah += 1

#     @property
#     def info(self):
#         return "{}  Level  :{} \n\tHealth :{}/{}\n\tPower  :{}\n\tDefense:{}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__power,self.__defense)

#     @property
#     def GainExp(self):
#         pass
    
#     @GainExp.setter
#     def GainExp(self,AddExp):
#         self.__exp += AddExp
#         if (self.__exp >= 100):
#             print(self.__name,"level Up")
#             self.__level += 1
#             self.__exp -= 100
            
#             self.__power = self.__powerStandar * self.__level
#             self.__defense = self.__defenseStandar * self.__level
#             self.__healthMax = (self.__healthStandar * self.__level)

#     def attack(self,enemy):
#         self.GainExp = 10  


# zilong = Hero('zilong',100,100,50)
# miya = Hero("miya",100,100,10)

# print(zilong.info)
# count = 0

# while count < 10:
#     miya.attack(zilong)
#     count += 1

# print(miya.info)


# class Hero():
#     def __init__(self,name,health,power,defense):
#         self.name = name
#         self.health = health 
#         self.power = power
#         self.defense = defense

#     def showinfo(self):
#         print(f"{self.name} memiliki power {self.power}\nmemiliki health {self.health}\nmemiliki defense {self.defense}\n")

# class Hero_Intelligent(Hero):
#     def __init__(self,name):
#         # Hero.__init__(self,name,100,300,100)
#         # Hero.showinfo(self)
#         #Atau
#         super().__init__(name,100,300,100)
#         # super().showinfo()

#         #Overriding
#     def showinfo(self):
#         print(f"{self.name} Tipe : Intelligent\nmemiliki power {self.power}\nmemiliki health {self.health}\nmemiliki defense {self.defense}\n")

# class Hero_Strength(Hero):
#     def __init__(self,name):
#         # Hero.__init__(self,name,200,100,200)
#         # Hero.showinfo(self)
#         #Atau
#         super().__init__(name,200,100,200)
#         # super().showinfo()

#         #Overriding
#     def showinfo(self):
#         print(f"{self.name} Tipe : Strength\nmemiliki power {self.power}\nmemiliki health {self.health}\nmemiliki defense {self.defense}\n")


# harley = Hero_Intelligent("Harley")
# balmond = Hero_Strength("Balmond")
# # print(harley.name," ",harley.power)
# # print(balmond.name," ",balmond.power)
# balmond.showinfo()
# harley.showinfo()



# class Hero:

# 	def __init__(self,name):
# 		self.health_pool = [0,100,200,300,400,500]
# 		self.attPower_pool = [0,10,20,30,40,50]
# 		self.armor_pool = [0,1,2,3,4,5]
# 		self.__name = name
# 		self.__exp = 0
# 		self.__level = 0

# 	def show_info(self):
# 		print("{} \n\tlevel: {}\n\thealth: {} \n\tattPower: {} \n\tarmor: {}".format(
# 				self.__name,
# 				self.__level,
# 				self.__health,
# 				self.__attPower,
# 				self.__armor
# 			)
# 		)

# 	@property
# 	def health_pool(self):
# 		pass

# 	@property
# 	def attPower_pool(self):
# 		pass

# 	@property
# 	def armor_pool(self):
# 		pass

# 	@property
# 	def levelUp(self):
# 		pass

# 	@property
# 	def gainExp(self):
# 		pass

# 	@health_pool.setter
# 	def health_pool(self,input):
# 		self.__health_pool = input

# 	@attPower_pool.setter
# 	def attPower_pool(self,input):
# 		self.__attPower_pool = input

# 	@armor_pool.setter
# 	def armor_pool(self,input):
# 		self.__armor_pool = input

# 	@gainExp.setter
# 	def gainExp(self,input):
# 		self.__exp += input
# 		if(self.__exp >= 100):
# 			self.levelUp = self.__exp//100
# 			self.__exp %= 100

# 	@levelUp.setter
# 	def levelUp(self,input):
# 		self.__level += input
# 		self.__health = self.__health_pool[self.__level]
# 		self.__attPower = self.__attPower_pool[self.__level]
# 		self.__armor = self.__armor_pool[self.__level]


# class HeroIntelligent(Hero):

# 	def __init__(self,name):
# 		super().__init__(name)
# 		self.health_pool = [0,50,100,150,200,250]
# 		self.attPower_pool = [0,20,40,60,80,100]
# 		self.armor_pool = [0,0.5,1,1.5,2,2.5]
# 		self.levelUp = 1


# class HeroStrength(Hero):

# 	def __init__(self,name):
# 		super().__init__(name)
# 		self.health_pool = [0,200,300,400,500,600]
# 		self.attPower_pool = [0,20,40,60,80,100]
# 		self.armor_pool = [0,2,4,6,8,10]
# 		self.levelUp = 1


# sniper = HeroIntelligent("sniper")
# sniper.show_info()


# method resolution order dan diamon problem

# class x:
# 	def murid_sekolah(self):
# 		print(f"Aku adalah Murid kelas x")

# class a(x):
# 	def murid_sekolah(self):
# 		print(f"Aku adalah Murid kelas a")

# class b(x):
# 	def murid_sekolah(self):
# 		print(f"Aku adalah Murid kelas b")

# class c(a,b): #yang diambil adalah yang pertama
# 	pass

# faqih = c()
# faqih.murid_sekolah()

#magic method

# class pisang:
# 	def __init__(self,jumlah):
# 		self.jumlah = jumlah

# 	def __repr__(self):
# 		return "Debug: Pisang ini berjumlah: {}".format(self.jumlah)

# 	def __str__(self):
# 		return "Pisang ini berjumlah: {}".format(self.jumlah)

# 	def __add__(self,objek):
# 		return self.jumlah + objek.jumlah

# 	@property
# 	def __dict__(self):
# 		return ("Objek ini memiliki jumlah: {}".format(self.jumlah))

# objek = pisang(10)
# objek2 = pisang(20)
# print(objek)
# print(objek2)
# print(repr(objek))
# print(repr(objek2))
# print(objek + objek2)
# print(objek.__dict__)
# print(objek2.__dict__)

#Abstract class
#Abc = abstract base class
from abc import ABC,abstractmethod

class Button:

	def __init__(self,set_link):
		self.link = set_link

	@abstractmethod
	def click(self):
		pass

	@property
	@abstractmethod
	def link(self):
		pass

class PushButton(Button):
	
	def click(self):
		print("go to: {}".format(self.link))

	@Button.link.setter
	def link(self,input):
		self.__link = input

	@link.getter
	def link(self):
		return self.__link

# class RadioButton(Button):

# 	def click(self):
# 		print("Click Radio Button")

tombol = PushButton("www.xsekutor.com")
tombol.click()



