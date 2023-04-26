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

game_object = GameObject("Knife","Some appareance","Some feel", "Some smell") 

game_object.name = "Spoon"
print(game_object.sniff())