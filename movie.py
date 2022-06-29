class Movie:
    def __init__(self, name):
        self.name = name
        
    def watch(self):
        print('Bon visionnage !' + self.name)
        
class TapeMovie(Movie):
    def __init__(self, name):
       super().__init__(name)


class DVD:
    def __init__(self, name):
        self.name = name
        
    def watch(self, type):
        print('Le CD: ' + self.name)
    
    def displayMenu(self):
        print('Menu Ouvert !')
        self.menu = True
        
    
class Blue_Ray(DVD):
    def watch(self, type):
    
    
        if type != 'PS4':
            print('Ce cd doit être mis dans une Playstation')
        else:
            print('CD mis dans la playstation')
        

movie = Movie("2008: Shutter Island")
k7 = TapeMovie("Scream")
videodisc = DVD("Les indestructibles")
blueray = Blue_Ray("PS4")

# movie.name
movie.watch()


k7.name
k7.watch()



videodisc.name
videodisc.watch(type)


blueray.name
blueray.watch('PS4')
blueray.displayMenu()


