#código extraido de un alumno de intro 100% real no fake

class pochamon:
	def __init__(self,nombre,hp,defensa,ataques):
		self.nombre=nombre
		self.hp=hp
		self.defens=defensa
		self.ataques=ataques
	def AtacarOtropochamon(self,otro):
		import random
		ataque=self.ataques[random.randint(0,len(self.ataques)-1)]
		ataque=self.ataques[0]
		otro.recibirAtaque(ataque)
		print("{} recibe el {} de {}!".format(otro.nombre,ataque[0],self.nombre))
	def recibirAtaque(self,ataque):
		self.hp-=ataque[1]
	def aparearse(self,pkmencelo):
		self.hp+=(self.pkmencelo.hp)/2
		print("tu pochamon se ha recuperado 1313")
		import random
		if random.randint(0,1)==1:
			print("Rayos, alguien no se cuido parece")
			nombre=input("Cómo debe llamarse la nueva criatura?")
			huevo = pochamon(nombre,100,100,[])
			return huevo
		else:
			print("Todo salio bien :D")
class entrenador_pochamon:
	def __init__(self,nombre):
		self.nombre=nombre
		self.pochamones=[]
	def Capturar(self,pochamon):
		print("Solo tiene 2 pochabolas")
		print("Lanza una...")
		import random
		val=random.randint(0,1)
		val=0 
		if val:
			print("{} capturado a {}".format(self.name,pochamon.nombre))
		else:
			print("Lastima, se te ha escapado, sigues solo sin pochamones ni amigos :)")
at=[("Sexy Naked Dance",30),("Fus Ro Dah",80),("Pocket Nuke",100),("Onda vital coñooo",150)] 
att=[("Saitama's Absolutly Normal Punch", 30),("Poroto con rienda", 80),("Fcking Minigun", 100),("Midterm de Programación Avanzada", 150)]
p=pochamon("Flóóryh",100,20,at)
pp=pochamon("Daedalus",80,50,att)
print("Batalla pochamon!")
print("Flóóryh ataca a Daedalus")
p.AtacarOtropochamon(pp)
e=entrenador_pochamon("Antonio")
print("Repentinamente el entrenado Antonio aparece e intenta capturar a Flooryh")
e.Capturar(p)
