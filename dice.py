import random # python de base ne sait pas faire d'aléatoir. Il faut importer un module pour cela (déjà prés instaler dans python).pour les utiliser il faut les appeler. (liste des module sur docs.python.org)

class Dice:

    label = "dice"

    def __init__(self, faces=6):
        self.faces = faces

    def __str__(self):
        return f"I'm a {type(self).label} with {self.faces} faces"   #type(self) permet de récupérer le type de l'objet ici la classe Dice c'est donc équivalent à Dice.label 
    
    def roll(self):
        return random.randint(1, self.faces) #une methode est toujours suivi de parenthèse
    
class RiggedDice(Dice): #class obtenu par héritage de dice pour en faire un dé truqué sans répéter le code de Dice. les class enfant quant elle vont réutiliser cette fonction vont ainsi remplacer automatiquement leur nom par le type de la classe via le label precider dans chaque class. 
    label = "rigged dice"
    def roll(self,rigged = False):#polymorphisme: on peut modifier une methode de la classe parente en la redéfinissant dans la classe fille
        
        if (rigged): 
            return self.faces
        else:
            return super().roll() #super() permet d'appeler la methode de la classe parente (Dice) de la ligne 13 sans la réécrire

#return self.faces if rigged else super().roll() #même chose que les 3 lignes précédentes


class WoodDice(Dice): 
    label = "Wood Dice"




# main

if __name__ == "__main__": #permet de savoir si on est dans le fichier dice.py ou si on l'importe dans un autre fichier. Si on est dans le fichier dice.py alors on execute le code en dessous. Si on l'importe dans un autre fichier alors on n'execute pas la partie main de ce fichier.

    print(f"variable name : {__name__}") #affiche __main__ car on est dans le fichier dice.py mais affiche le nom du fichier (dice)si on l'importe dans un autre fichier.

    a_dice = Dice()
    print(a_dice)

    a_dice = RiggedDice()
    print(a_dice)

    a_wood_dice = WoodDice()
    print(a_wood_dice)

    for i in range(0, 10): #range est une fonction qui permet de faire une boucle de 10 étiration qui part de 0 jusqu'à 9 (10 non compris)
        print(a_dice.roll(true))
