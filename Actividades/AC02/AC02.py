
if __name__ == '__main__':
    animals = list()
    animals.append(GoldenPUC(expresion=0.5, nombre="Mara", color="Blanco", sexo="Hembra"))
    animals.append(GoldenPUC(expresion=0.9, nombre="Eddie", color="Rubio", sexo="Macho"))
    animals.append(SiamePUC(expresion=0.9, nombre="Felix", color="Naranjo", sexo="Hembra"))
    animals.append(PUCTerrier(expresion=0.8, nombre="Betty", color="Café", sexo="Hembra"))

    for a in animals:
        print(a)
        a.jugar()
        a.comer()