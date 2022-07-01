
class User():
    def __init__(self, name, password ) -> None:
        if len(name) < 2:
            raise UsernameError()
        if len(password) < 10:
            raise PasswordError()
        self.name = name
        self.password = password

class UsernameError(Exception):
    
    def __init__(self, msg="", *args, **kwargs):
        msg = msg or "Username too short"
        super().__init__(msg, *args, **kwargs)

class PasswordError(Exception):
    def __init__(self, msg="", *args, **kwargs):
        msg = msg or "Password too short"
        super().__init__(msg, *args, **kwargs)




Leo = User('Yessirbaby', 'OPOPOOPOPOO')

print(str(Leo.name) + ' is connected')