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
    # default values: not technically required, but suggested.
    hitpoints = 1  # default hitpoints > 0 implies critter is alive
    damage = 0     # note: here, damage will not give an exception...in critter
    
    def __init__(self, name):
        self.name = name
    
    def is_alive(self):
        return self.hitpoints > 0
    
    def select_target(self, creatures):
        ''' When there's more than one creature to fight, 
            an attacker has to choose.             
        '''  
        
        if isinstance(self, Goblin) or isinstance(self, Ewok):
            ''' When there's more than one creature to fight, 
                an attacker has to choose. Goblins and Ewoks 
                simply choose the first one in the list
                
                Goblins have one last trick. Generations of conflict 
                with Orcs have taught them especially effective tactics 
                against their long-time foes. So when they attack an 
                Orc - *any* kind of Orc - they deal double damage:
            '''
            #print(f'I am a {self.__class__.__name__}')
            for c in creatures:
                if c == self:
                   pass
                else:
                   attacked = c
                   if isinstance(self, Goblin) \
                       and ( isinstance(attacked, Orc) \
                           or isinstance(attacked, HillOrc) ):
                               self.damage = 2 * self.damage
                   return attacked
                    
               
        elif isinstance(self, Skeleton):
            ''' Skeletons are more devious and opportunistic. 
            They will choose the creature in the list with 
            the fewest hit points
            '''
            #print(f'I am a {self.__class__.__name__}')
            #creatures_hitpoints = [c.hitpoints for c in creatures]
            #print(creatures_hitpoints)
            creatures_sorted = sorted(creatures, key=lambda x: x.hitpoints)
            #print([c.hitpoints for c in creatures_sorted])
            for c in creatures_sorted:
                if c == self:
                    pass
                else:
                    attacked = c
                    return attacked
                    
            
        elif isinstance(self, Orc) or isinstance(self, HillOrc):
            ''' Orcs (including Hill Orcs) are more complex. First, 
            they won't attack other orcs at all... unless there's 
            no one to attack *except* an orc. And among those it's 
            willing to attack, it will pick the one with the worst 
            armor
            '''
            # sort creatures in rank of worst armor
            #print(sorted(creatures, key=lambda x: x.armor, reverse=False))
            creatures_worst_armor = \
                    sorted(creatures, \
                           key=lambda x: x.armor, \
                               reverse=False)
                    
            # determine if the list of creatures are only Orcs
            length_creatures = len(creatures_worst_armor)
            orc_test = []
            for cwa in creatures_worst_armor:
                if isinstance(cwa, Orc) or isinstance(cwa, HillOrc):
                    orc_test.append(True)
                else:
                    orc_test.append(False)
            if sum(orc_test) == length_creatures and creatures[0] != self:
                return creatures_worst_armor.pop(0)
                
            
            # iterate on creatures according to rank        
            for c in creatures_worst_armor:
                if isinstance(c, Orc):  # note this will pass on c == self
                    pass
                else:
                    attacked = c
                    return attacked                                                           
                    # if isinstance(self, HillOrc) and \
                    #               isinstance(attacked, Skeleton):
                    #     ''' Hill Orcs have a weakness. Though strong and tough, 
                    #     they are TERRIFIED of skeletons. If they attack one, 
                    #     fear reduces their muscles to jelly, and they do no 
                    #     damage at all:                                     
                    #     '''
                    #     self.hitpoints = 0
                    # elif isinstance(self, HillOrc) and \
                    #               not isinstance(attacked, Skeleton):
                    #     self.hitpoints = 20

                
        else:
            print('ERROR:  I am not defined')                                       
        
    def attack(self, target): 
        '''
        The hitpoints, damage and armor values come into play when the
        creatures fight.  The total damage done is equal to the attacker's
        "damage" value, minus the target's "armor" value. The attack() method
        returns the net damage done
        '''
        # note how we have a net damage (damage) and a self.damage associated
        # with the instance object (e.g. Orc and Goblin)
        
        if ( isinstance(self, Orc) \
            or isinstance(self, HillOrc) ) \
                and isinstance(target, Skeleton):
            damage = 0 
            return damage
        
        damage = self.damage - target.armor
        if damage >= target.hitpoints:
            damage = target.hitpoints
        target.hitpoints -= damage

        return damage
       
    
    def describe(self):
        return f'{self.name.capitalize()} the {self.__class__.__name__}'
        
    
class Goblin(Creature):
    ''' Goblin critter '''
    hitpoints = 10
    damage = 3
    armor = 1
        
class Orc(Creature):
    ''' Orc critter '''
    hitpoints = 15
    damage = 5
    armor = 2
    
class HillOrc(Orc):
    ''' A HillOrc is a subclass of Orc '''
    hitpoints = 20
    damage = 5
    armor = 3    
    
class Skeleton(Creature):
    ''' Orc critter '''
    hitpoints = 8
    damage = 4
    armor = 0    
    
class Ewok(Creature):
    ''' Orc critter '''
    hitpoints = 4
    damage = 10
    armor = 1     
    
   

# command code:
goby = Goblin('Goby')
goby.name
goby.hitpoints    
goby.armor

morgash = Orc('Morgash')
morgash.name
morgash.hitpoints
morgash.damage
morgash.armor

narbul = HillOrc('Narbul')
narbul.name
narbul.hitpoints
narbul.damage
narbul.armor

bonez = Skeleton('Bonez')
bonez.name
bonez.hitpoints
bonez.damage
bonez.armor

teebo = Ewok('Teebo')
teebo.name
teebo.hitpoints
teebo.damage
teebo.armor

isinstance(goby, Creature)
isinstance(morgash, Creature)
isinstance(narbul, Creature)
# print(isinstance(narbul, HillOrc))
isinstance(bonez, Creature)
isinstance(teebo, Creature)

print(bonez.is_alive())
bonez.hitpoints = 0
print(bonez.is_alive())
bonez.hitpoints = 8
print(bonez.is_alive())

goby.hitpoints       # 10
bonez.hitpoints      # 8
bonez.attack(goby)   # 3
goby.hitpoints       # 7

# Skeletons have no armor, so they take the full impact!
print(goby.attack(bonez))

print(bonez.hitpoints) 


creatures = [narbul, goby, teebo, bonez, morgash]
# for c in creatures:
#     if isinstance(c, Orc):
#         print(f'I am an {c}')
        
#for c in creatures:
#    print(type(c))

#    print(c)
target = goby.select_target(creatures)
print(target.name)
# 'Narbul'

target = teebo.select_target(creatures)
print(target.name)
# 'Narbul'

target = bonez.select_target(creatures)
print(target.name)
# 'Teebo'

target = narbul.select_target(creatures)
print(target.name)
# 'Bonez'

only_orcs = [narbul, morgash]
nashba = Orc('Nashba')
# print(f'narbul armor = {narbul.armor}')
# print(f'nashba armor = {nashba.armor}')
# print(f'morgash armor = {morgash.armor}')
target = nashba.select_target(only_orcs)
print(target.name)
#'Morgash'

bonez.hitpoints
# 5
print(narbul.attack(bonez))
# 0
print(narbul.attack(bonez))
# 0
print(narbul.attack(bonez))
# 0
print(bonez.hitpoints)
# 5

print(nashba.hitpoints)
# 15
print(goby.attack(nashba))
# 4
print(nashba.hitpoints)
# 11

#  make corrections below:
print(narbul.hitpoints)
#20
print(goby.attack(narbul))
#3
print(narbul.hitpoints)
# 17

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
