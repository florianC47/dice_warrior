import random

from caracter import Warrior, Mage, Rogue, Caracter
from dice import Dice
from rich.console import Console

def main():
        warrior= Warrior("james",20, 8 ,3, Dice(6))
        mage = Mage("Elise",20, 8 ,3, Dice(6))
        rogue= Rogue("Rogue",20, 8 ,3, Dice(6))

        cars= [warrior, mage, rogue]
        stats = {}

        car1: Caracter = random.choice(cars) #random.choice permet de choisir un élément au hasard dans une liste ; le type Caracter permet de préciser que la variable car1 est de type Caracter
        cars.remove(car1) #remove permet de supprimer l'elemnt qui aura été tiré pour ne pas lui permettre de combatre contre lui lors du tirage de l'adversaire
        car2: Caracter = random.choice(cars) #tirage de l'adversaire
        cars.remove(car2)

        print(car1)
        print(car2)

        stats[car1.get_label()] = 0
        stats[car2.get_label()] = 0

        print(stats)

        for i in range(0, 50):
            car1.regenerate() #on regenere les pv des joueurs car sinon il garderai la vie restante du precedent combat
            car2.regenerate()
            while (car1.is_alive() and car2.is_alive()):
                car1.attack(car2)
                car2.attack(car1)
            if (car1.is_alive()):
                 stats [car1.get_label()] += 1
            else:
                 stats [car2.get_label()] += 1

        print(stats)

if __name__ == "__main__":
    main()