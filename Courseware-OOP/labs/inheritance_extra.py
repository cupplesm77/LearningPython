'''

Riding the massive breakout success of your first game, Orcs
Vs. Goblins, your team dives right into developing its sequel:
Creature Clash. This new game features many new creature types... as
well as the classic goblins:

>>> goby = Goblin('Goby')
>>> goby.name
'Goby'

Like all creatures in this new game, Goblins have attributes for their
hitpoints, attack damage, and defensive armor.

>>> goby.hitpoints
10
>>> goby.damage
3
>>> goby.armor
1

Of course, your fan base will rebel if you don't also have orcs. Like
before, they're a bit tougher:

>>> morgash = Orc('Morgash')
>>> morgash.name
'Morgash'
>>> morgash.hitpoints
15
>>> morgash.damage
5
>>> morgash.armor
2

And now we introduce HillOrcs, who are even tougher (but with a
weakness you'll learn about later):

>>> narbul = HillOrc('Narbul')
>>> narbul.name
'Narbul'
>>> narbul.hitpoints
20
>>> narbul.damage
5
>>> narbul.armor
3

There's also skeletons, who don't have any armor at all:

>>> bonez = Skeleton('Bonez')
>>> bonez.name
'Bonez'
>>> bonez.hitpoints
8
>>> bonez.damage
4
>>> bonez.armor
0

And finally, Ewoks. Who are tiny, but pack a punch (by
creating clever, devastating traps):

>>> teebo = Ewok('Teebo')
>>> teebo.name
'Teebo'
>>> teebo.hitpoints
4
>>> teebo.damage
10
>>> teebo.armor
1

Each of these inherit from a class called Creature. In writing your
code, be sure to put as many methods and member variables as possible
in this base class, overriding in the subclass when necessary.

>>> isinstance(goby, Creature)
True
>>> isinstance(morgash, Creature)
True
>>> isinstance(narbul, Creature)
True
>>> isinstance(bonez, Creature)
True
>>> isinstance(teebo, Creature)
True

You can check whether a creature is alive:

>>> bonez.is_alive()
True
>>> bonez.hitpoints = 0
>>> bonez.is_alive()
False
>>> bonez.hitpoints = 8
>>> bonez.is_alive()
True

The hitpoints, damage and armor values come into play when the
creatures fight.  The total damage done is equal to the attacker's
"damage" value, minus the target's "armor" value. The attack() method
returns the net damage done:

>>> goby.hitpoints
10
>>> bonez.hitpoints
8
>>> bonez.attack(goby)
3
>>> goby.hitpoints
7

Skeletons have no armor, so they take the full impact!
>>> goby.attack(bonez)
3
>>> bonez.hitpoints
5

When there's more than one creature to fight, an attacker has to
choose. Goblins and Ewoks simply choose the first one in the list:

>>> creatures = [narbul, goby, teebo, bonez, morgash]
>>> target = goby.select_target(creatures)
>>> target.name
'Narbul'
>>> target = teebo.select_target(creatures)
>>> target.name
'Narbul'

Skeletons are more devious and opportunistic. They will choose the
creature in the list with the fewest hit points:

>>> target = bonez.select_target(creatures)
>>> target.name
'Teebo'

Orcs (including Hill Orcs) are more complex. First, they won't attack
other orcs at all... unless there's no one to attack *except* an
orc. And among those it's willing to attack, it will pick the one with
the worst armor:

>>> target = narbul.select_target(creatures)
>>> target.name
'Bonez'
>>> target = morgash.select_target(creatures)
>>> target.name
'Bonez'

If there's no one to attack BUT orcs, then an orc will happily attack
the one with the worst (lowest) armor:

>>> only_orcs = [narbul, morgash]
>>> nashba = Orc('Nashba')
>>> target = nashba.select_target(only_orcs)
>>> target.name
'Morgash'

Hill Orcs have a weakness. Though strong and tough, they are TERRIFIED of
skeletons. If they attack one, fear reduces their muscles to jelly, and they do
no damage at all:

>>> bonez.hitpoints
5
>>> narbul.attack(bonez)
0
>>> narbul.attack(bonez)
0
>>> narbul.attack(bonez)
0
>>> bonez.hitpoints
5

Goblins have one last trick. Generations of conflict with Orcs have
taught them especially effective tactics against their long-time
foes. So when they attack an Orc - *any* kind of Orc - they deal
double damage:

>>> nashba.hitpoints
15
>>> goby.attack(nashba)
4
>>> nashba.hitpoints
11

>>> narbul.hitpoints
20
>>> goby.attack(narbul)
3
>>> narbul.hitpoints
17

'''

# Write your code here:
class Creature:
    ''' Baseclass '''
    
    # In later versions of Python 3, you can declare member variables
    # and their intended types, like this:
    name: str
    hitpoints: int
    damage: int
    armor: int
    # This isn't necessary, and Python doesn't enforce the types.
    # It's current main use is documentation, essentially.
    # (But for extra-extra credit, check out the "mypy" project.)    
    
    # default values: not technically required, but suggested.
    hitpoints = 1  # default hitpoints > 0 implies critter is alive
    damage = 0   # note: here, damage will not give an exception...in creature
    
    def __init__(self, name):
        self.name = name
    
    def is_alive(self):
        return self.hitpoints > 0
        
    def attack(self, enemy):
        ''' The hitpoints, damage and armor values come into play when the
        creatures fight.  The total damage done is equal to the attacker's
        "damage" value, minus the target's "armor" value. The attack() method
        returns the net damage done:
        '''    
        # note how we have a local damage (damage) and a self.damage 
        # associated with the instance object (e.g. Orc and Goblin)
        damage = self.damage
        return self._simple_damage(enemy, damage)
            
    
    def _simple_damage(self, enemy, damage):   
        # note how we have a local damage (damage) and a self.damage 
        # associated with the instance object (e.g. Orc and Goblin)
        damage -= enemy.armor
        # we never allow damage to become < 0
        if damage < 0:
            damage = 0            
        # note that we allow hitpoints to become negative    
        enemy.hitpoints -= damage
        return damage
        

    
    def select_target(self, creatures):
        return creatures[0]
    
    def describe(self):
        return f'{self.name.capitalize()} the {self.__class__.__name__}'
        
    
class Goblin(Creature):
    ''' Goblin critter '''
    hitpoints = 10
    damage = 3
    armor = 1
    
    def attack(self, enemy):
        ''' The hitpoints, damage and armor values come into play when the
        creatures fight.  The total damage done is equal to the attacker's
        "damage" value, minus the target's "armor" value. The attack() method
        returns the net damage done:
            
        Goblins have one last trick. Generations of conflict with Orcs have
        taught them especially effective tactics against their long-time
        foes. So when they attack an Orc - *any* kind of Orc - they deal
        double damage:            
        '''    
        # note how we have a local damage (damage) and a self.damage 
        # associated with the instance object (e.g. Orc and Goblin)
        
        damage = self.damage
        if isinstance(enemy, Orc):
            damage = 2 * damage            
                
        return self._simple_damage(enemy, damage)        
        
class Orc(Creature):
    ''' Orc critter '''
    hitpoints = 15
    damage = 5
    armor = 2
    
    ''' Orcs (including Hill Orcs) are more complex. First, 
    they won't attack other orcs at all... unless there's 
    no one to attack *except* an orc. And among those it's 
    willing to attack, it will pick the one with the worst 
    armor
    '''
    def select_target(self, creatures):
        # sort creatures in rank of worst armor
        #print(sorted(creatures, key=lambda x: x.armor, reverse=False))
        creatures_worst_armor = \
                sorted(creatures, \
                       key=lambda x: x.armor, \
                           reverse=False)            
        
                    
        # not Orcs (and therefore not self)
        not_orcs = [c for c in creatures_worst_armor if not isinstance(c, Orc)]                    
                
        # set the list of enemies
        length_not_orcs = len(not_orcs)
        if length_not_orcs == 0:
            enemies = creatures_worst_armor
        else:
            enemies = not_orcs
         
        return enemies[0]

    
class HillOrc(Orc):
    ''' A HillOrc is a subclass of Orc '''
    hitpoints = 20
    damage = 5
    armor = 3   
    
    def attack(self, enemy):
        ''' The hitpoints, damage and armor values come into play when the
        creatures fight.  The total damage done is equal to the attacker's
        "damage" value, minus the target's "armor" value. The attack() method
        returns the net damage done:
        '''    
        # special case of HillOrc attacking a Skeleton
        # Hill Orcs have a weakness. Though strong and tough, they are 
        # TERRIFIED of skeletons. If they attack one, fear reduces their 
        # muscles to jelly, and they do no damage at all:
        damage = self.damage            
        if isinstance(enemy, Skeleton):
            damage = 0                                  
        
        return self._simple_damage(enemy, damage)   
    
    
class Skeleton(Creature):
    ''' Orc critter '''
    hitpoints = 8
    damage = 4
    armor = 0    
    
    # Skeletons are more devious and opportunistic. They will choose the
    # creature in the list with the fewest hit points:
    def select_target(self, creatures):
        creatures_min = sorted(creatures, key=lambda x: x.hitpoints)
        #weakest = min(creatures, key=lambda enemy: enemy.hitpoints)
        for c in creatures_min:
            if c == self:
                pass
            else:
                attacked = c
                return attacked     
                       

class Ewok(Creature):
    ''' Orc critter '''
    hitpoints = 4
    damage = 10
    armor = 1     

# commands
goby = Goblin('Goby')
goby.name

#   Like all creatures in this new game, Goblins have attributes for their
#   hitpoints, attack damage, and defensive armor.

goby.hitpoints
goby.damage
goby.armor

# Of course, your fan base will rebel if you don't also have orcs. Like
# before, they're a bit tougher:

morgash = Orc('Morgash')
morgash.name
'Morgash'
morgash.hitpoints
morgash.damage
morgash.armor

narbul = HillOrc('Narbul')
narbul.name
narbul.hitpoints
narbul.damage
narbul.armor

# there's also skeletons, who don't have any armor at all:
bonez = Skeleton('Bonez')
bonez.name
bonez.hitpoints
bonez.damage
bonez.armor

# And finally, Ewoks. Who are tiny, but pack a punch (by
# creating clever, devastating traps):

teebo = Ewok('Teebo')
teebo.name
teebo.hitpoints
teebo.damage
teebo.armor

# each of these inherit from a class called Creature. In writing your
#code, be sure to put as many methods and member variables as possible
# in this base class, overriding in the subclass when necessary.
print(isinstance(goby, Creature))
print(isinstance(morgash, Creature))
print(isinstance(narbul, Creature))
print(isinstance(bonez, Creature))
print(isinstance(teebo, Creature))

# You can check whether a creature is aliv
print(bonez.is_alive())
bonez.hitpoints = 0
print(bonez.is_alive())
bonez.hitpoints = 8
bonez.is_alive()

# The hitpoints, damage and armor values come into play when the
# creatures fight.  The total damage done is equal to the attacker's
# "damage" value, minus the target's "armor" value. The attack() method
# returns the net damage done:

    
# ******* Fix ***************
print(goby.hitpoints)
print(goby.armor)
# 10
# 1
print(bonez.hitpoints)
print(bonez.damage)
# 8
# 4
print(bonez.attack(goby))
# 3
print(goby.hitpoints)
# 7

# Skeletons have no armor, so they take the full impact!
goby.attack(bonez)
bonez.hitpoints

# When there's more than one creature to fight, an attacker has to
# choose. Goblins and Ewoks simply choose the first one in the list:
creatures = [narbul, goby, teebo, bonez, morgash]
target = goby.select_target(creatures)
print(target.name)
# 'Narbul'
target = teebo.select_target(creatures)
print(target.name)
# 'Narbul'

# Skeletons are more devious and opportunistic. They will choose the
# creature in the list with the fewest hit points:

target = bonez.select_target(creatures)
print(target.name)
# 'Teebo'

# Orcs (including Hill Orcs) are more complex. First, they won't attack
# other orcs at all... unless there's no one to attack *except* an
# orc. And among those it's willing to attack, it will pick the one with
# the worst armor:

target = narbul.select_target(creatures)
print(target.name)
# 'Bonez'
target = morgash.select_target(creatures)
print(target.name)
# 'Bonez'

# If there's no one to attack BUT orcs, then an orc will happily attack
# the one with the worst (lowest) armor:

only_orcs = [narbul, morgash]
nashba = Orc('Nashba')
print(nashba.hitpoints)
target = nashba.select_target(only_orcs)
print(target.name)
#'Morgash'

# Hill Orcs have a weakness. Though strong and tough, they are TERRIFIED of
# skeletons. If they attack one, fear reduces their muscles to jelly, and they
# do no damage at all:

bonez.hitpoints
# 5
narbul.attack(bonez)
# 0
narbul.attack(bonez)
# 0
narbul.attack(bonez)
# 0
bonez.hitpoints
# 5

# Goblins have one last trick. Generations of conflict with Orcs have
# taught them especially effective tactics against their long-time
# foes. So when they attack an Orc - *any* kind of Orc - they deal
# double damage:

print(nashba.hitpoints)
# 15
goby.attack(nashba)
# 4
nashba.hitpoints
# 11

narbul.hitpoints
# 20
goby.attack(narbul)
#3
narbul.hitpoints
# 17

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
