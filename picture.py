class Picture:
    def __init__(self, name):
        self.name = name
        print('The name of this picture is: ' + name)
    def show(self, to_show):
        print('The format of this picture is: ' + str(to_show))    
        
class PNG(Picture):
    def __init__(self, name):
        super().__init__(name)
    def show(self, to_show):
        return super().show(to_show)    

class GIF(Picture):
    def __init__(self, name):
        super().__init__(name)     
    
    def show(self, to_show):
        return super().show(to_show)
    
    
    
    
    
format1 = PNG('Coucou')
format2 = GIF('MOTHERFUCKER')

# print(format1.show('name'))
# print(format2)

format1.show('PNG')
format2.show('GIF')


