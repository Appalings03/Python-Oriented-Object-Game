class GameObject:    
    def __init__(self, name, apperance, feel, smell):
        self.name = name
        self.apperance = apperance
        self.feel = feel
        self.smell = smell
    
    def look(self):
        return f"You look at the {self.name}. {self.apperance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"

'''
game_object = GameObject("Knife","Some appareance","Some feel", "Some smell") 

game_object.name = "Spoon"
print(game_object.sniff())
'''

class Room :
    escape_code = 0
    game_objects = []

    def __init__(self, escape_code,game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return self.escape_code == code

    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names