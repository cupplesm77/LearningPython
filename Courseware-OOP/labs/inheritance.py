'''

Imagine writing a game called Orcs Vs. Goblins. You will, of course,
need goblins:

>>> goby = Goblin('Goby')
>>> goby.name
'Goby'

>>> goby.hitpoints
10
>>> goby.damage
3

You'll also need orcs, who are a bit bigger and tougher:

>>> morgash = Orc('Morgash')
>>> morgash.name
'Morgash'
>>> morgash.hitpoints
15
>>> morgash.damage
5

You can check whether a creature is alive:

>>> morgash.is_alive()
True
>>> morgash.hitpoints = 0
>>> morgash.is_alive()
False
>>> morgash.hitpoints = 10
>>> morgash.is_alive()
True

Both goblins and orcs inherit from a class called Critter.
IMPORTANT: Put as many methods and member variables as possible in
this base class. Can you find a way to put ALL the methods in Critter?

>>> isinstance(goby, Critter)
True
>>> isinstance(morgash, Critter)
True

This being a fighting game, critters can (and will) attack each other.
(Notice the attack() method returns the amount of damage done.)

>>> goby.hitpoints
10
>>> morgash.hitpoints
10
>>> morgash.attack(goby)
5
>>> goby.hitpoints
5
>>> goby.attack(morgash)
3
>>> goby.attack(morgash)
3
>>> morgash.hitpoints
4

Hit points can't go below zero, though:
>>> goby.attack(morgash)
3
>>> morgash.hitpoints
1
>>> goby.attack(morgash)
1
>>> morgash.hitpoints
0
>>> goby.attack(morgash)
0
>>> morgash.hitpoints
0

Critters can describe themselves, which we'll use in the user interface:

>>> goby.describe()
'Goby the Goblin'
>>> morgash.describe()
'Morgash the Orc'

'''

# Write your code here:
   
class Critter:
    ''' Baseclass '''
    
    # default values: not technically required, but suggested.
    hitpoints = 1  # default hitpoints > 0 implies critter is alive
    damage = 0     # note: here, damage will not give an exception...in critter
    
    def __init__(self, name):
        self.name = name
    
    def is_alive(self):
        return self.hitpoints > 0
        
    def attack(self, defender):
        # note how we have a local damage (damage) and a self.damage associated
        # with the instance object (e.g. Orc and Goblin)
        damage = self.damage
        if damage > defender.hitpoints:
            damage = defender.hitpoints
        defender.hitpoints -= damage    
        return damage
    
    def describe(self):
        return f'{self.name.capitalize()} the {self.__class__.__name__}'
        
    
class Goblin(Critter):
    ''' Goblin critter '''
    hitpoints = 10
    damage = 3
        
class Orc(Critter):
    ''' Orc critter '''
    hitpoints = 15
    damage = 5

        
# critter1 = Critter('MrCritter')
# print(critter1.name)
# print(critter1.is_alive())

goby = Goblin('Goby')
goby.name
goby.hitpoints
goby.damage

morgash = Orc('Morgash')
morgash.name
morgash.hitpoints
morgash.damage
morgash.is_alive()
morgash.hitpoints = 0
morgash.is_alive()
morgash.hitpoints = 10
morgash.is_alive()

print(isinstance(goby, Critter))
print(isinstance(morgash, Critter))

print(goby.hitpoints)        # 10
print(morgash.hitpoints)     # 10

print(morgash.attack(goby))  # 5
print(goby.hitpoints)        # 5

print(goby.attack(morgash))  # 3
print(goby.attack(morgash))  # 3
print(morgash.hitpoints)     # 4

print(goby.attack(morgash))  # 3
print(morgash.hitpoints)     # 1

print(goby.attack(morgash))  # 1
print(morgash.hitpoints)     # 0

print(goby.attack(morgash))  # 0
print(morgash.hitpoints)     # 0


# print(goby.hitpoints)
# print(morgash.hitpoints)

# print(goby.damage)
# print(morgash.damage)


print(goby.describe())              # 'Goby the Goblin'
print(morgash.describe())           # 'Morgash the Orc'


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
