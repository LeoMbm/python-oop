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
        
Leo = Personnages(100)
print(Leo.hp)
Leo.gettingHit(8)
Leo.gettingHit(3)
Leo.gettingHit(75)
print(Leo.hp)
Seb = Personnages(20)
print(Seb.hp)
Seb.gettingHit(8)
Seb.gettingHit(2)
Seb.gettingHit(10)
print(Seb.hp)