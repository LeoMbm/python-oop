class Tools:
    def __init__(self, tool):
        """Initialise les outils."""
        self.tools = [tool]
    def addTools(self, tool):
        self.tools.append(tool)
        print(tool + ' Added !')
    def removeTools(self, tools):
        index = self.tools.index(tool)
        del self.tools[index]
    

class Marteau:
    def __init__(self, color):
        self.color = color
        
    def paint(self, color):
        print('Paint in ' + color)
        
    def hammer_in(nail):
        nail.hammer_in()
    def remove(nail):
        nail.remove()
   
    color = 'red', 'blue', 'yellow'
    
class Tournevis:
    def __init__(self, color):
        print('The screw is ' + color)
    def tighten(screw):
        screw.tighten()
    def loosen(screw):
        screw.loosen()
    size = 2
    
    
tool = Marteau('green')
new = Marteau('lol')
screw = Tournevis('Brown')
toolBox = Tools('Color') 

print(new.paint('yellow'))
print(tool.color)
tool.color = "No color"
print(toolBox.addTools('visseuse'))
print(tool.color)



# print(toolBox.addTools('yes'))