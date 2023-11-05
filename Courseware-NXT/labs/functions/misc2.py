# misc2.py

class Vertebrate:
    y = 'Vertebrate'

    def print_type(self):
        self.type = Vertebrate.y
        print(self.type)

class Animal(Vertebrate):
    def __init__(self, name):
        self.name = name
        self.type = Vertebrate.y

    def print_animal(self):
        print(self.name)
        print(self.type)

vertebrate = Vertebrate()
vertebrate.print_type()
deer = Animal("Running_Deer")
deer.print_animal()

