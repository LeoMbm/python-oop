class Voiture:
    def __init__(self, couleur):
        self.couleur = couleur
        
    def getColor(self):
        return self.couleur
    
    
Skoda = Voiture('Red')
print(Skoda.getColor())



class Personnages:
    def __init__(self, hp):
        self.hp = hp
    def gettingHit(self, life):
        self.hp = self.hp - life
        if self.hp <= 0:
            print('You are dead')
        else:
            print('You are: ' + str(self.hp) + 'HP')
        
Leo = Personnages(100)
print(str(Leo.hp) + ' Leo HP')
Leo.gettingHit(8)
Leo.gettingHit(3)
Leo.gettingHit(24)
print('End ' + str(Leo.hp) + ' Leo HP')



Seb = Personnages(100)
print(str(Seb.hp) + ' Seb HP')
Seb.gettingHit(8)
Seb.gettingHit(2)
Seb.gettingHit(65)
print('End ' + str(Seb.hp) + ' Seb HP')