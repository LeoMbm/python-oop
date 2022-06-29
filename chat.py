class Users:
    def __init__(self, username):
        self.username = username
        self.connected = True
        print(username +  ' is online')
class Modo:
    def __init__(self, username):
        self.username = username
        self.connected = True
        print(username +  ' is online')
class Human(Users, Modo):
    pass



user1 = Human('user normal')
user2 = Human('modo')



class Messages:
    def __init__(self, username):
            self.username = username
            
    def say(self, to_say):
        print(str(self.username) + ' told: ' + to_say)
class Answers:
        def __init__(self, username):
            self.username = username
            
        def answer(self, to_say):
            print(str(self.username) + ' told: ' + to_say)
        
        
            
class Feed(Answers, Messages):
    def say(self, to_say):
         return super().say(to_say)
    def answer(self, to_say):
         return super().answer(to_say)


user = Feed(user1.username)
modo = Feed(user2.username)

user.say(' Hello whats the best programming language?')
modo.answer('All')
user.say('Do you have some coins?')
modo.answer('I will delete your messages is not allowed in this forum')