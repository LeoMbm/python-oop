class Tools:
    def addTools():
       print('Hey from addTools')
    def removeTools(self, tools):
        self.tools = tools
    tools = 'Marteau, Tournevis'

class Marteau:
    def __init__(self, color):
        self.color = color
        
    def paint(self, color):
        print('Paint in ' + color)
        
    def hammer_in(self, nail):
        pass
    def remove(self, nail):
        pass
   
    color = 'red', 'blue', 'yellow'
    
class Tournevis:
    def __init__(self):
        pass
    def tighten(screw):
        pass
    def loosen(screw):
        pass
    size = 2
    
    
    
tool = Marteau('green')
new = Marteau('lol')

print(new.paint('yellow'))
print(tool.color)
Tools.addTools()