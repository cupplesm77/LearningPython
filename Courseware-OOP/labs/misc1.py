# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:36:09 2023

@author: gravi
"""

# ************************ ClassMethods ************************************

class Officer():
    RANK_DEFAULT = "Colonel"
    NAME_DEFAULT = "John Wayne"
    AGE_DEFAULT = 37

    def __init__(self, name=NAME_DEFAULT, age=AGE_DEFAULT, rank=RANK_DEFAULT):
        self.name = name
        self.age = age
        self.rank = rank

    @classmethod
    def interface_one(cls, last_name=NAME_DEFAULT, age=AGE_DEFAULT, rank=RANK_DEFAULT):
        """
        Alternative constructor
        Parameters
        """
        name = last_name
        return cls(name, age, rank)

    @classmethod
    def interface_two(cls, name, rank):
        """
        An alternative contructor:
        A different interface than interface_one and the baseclass interface
        Only includes name and rank call list parameters
        """
        name = name
        age = cls.AGE_DEFAULT
        rank = rank
        return cls(name, age, rank)

    @classmethod
    def change_default_age(cls, new_age):
        """
        Changing class default parameter: age
        """
        cls.AGE_DEFAULT = new_age

    @classmethod
    def change_default_rank(cls, new_rank):
        """
        Changing class default parameter: rank
        """
        cls.RANK_DEFAULT = new_rank

class Marine(Officer):
    @classmethod
    def interface_one(cls, name=Officer.NAME_DEFAULT, rank=Officer.RANK_DEFAULT, age=Officer.AGE_DEFAULT):
        return cls(name, age, rank)


class Army(Officer):
    @classmethod
    def interface_two(cls, name=Officer.NAME_DEFAULT, rank=Officer.RANK_DEFAULT):
        age = cls.AGE_DEFAULT
        return cls(name, age, rank)


marine_officer0 = Marine.interface_one()
print(marine_officer0.name)
print(marine_officer0.age)
print(marine_officer0.rank)

print("")
army_officer0 = Army.interface_one()
print(army_officer0.name)
print(army_officer0.age)
print(army_officer0.rank)

officer1 = Marine.interface_one("Cupples", "Colonel", 41)
print(officer1.name)
print(officer1.age)
print(officer1.rank)
print(f"Officer1's first age: {officer1.age}")
officer1.age = officer1.AGE_DEFAULT
print(f"Officer1's revised age: {officer1.age}")
officer1.change_default_age(47)
officer1.age = officer1.AGE_DEFAULT
print(f"Officer1's revised age: {officer1.age}")
officer1.age = 41
print(f"Officer1's revised age: {officer1.age}")

print("")
officer2 = Marine.interface_one("Curtis", "Major", 29)
print(officer2.name)
print(officer2.rank)
print(officer2.age)
print(f"officer2's current age: {officer2.age}")
print(f"officer2's AGE_DEFAULT age: {officer2.AGE_DEFAULT}")
officer2.change_default_rank("General")
officer2.rank = officer2.RANK_DEFAULT
officer2.age = officer2.AGE_DEFAULT
print(f"Officer2's revised rank: {officer2.rank}")
print(f"Officer2's revised age: {officer2.age}")

print("")
officer3 = Army.interface_two("Jones", "Colonel")
print(officer3.name)
print(officer3.rank)
print(officer3.age)
print(f"officer2's current age: {officer3.age}")

# ************************ ClassMethods: END ************************************

s = {2 ** x for x in range(10)}


class A():
    def __init__(self, x):
        self.x = x


class B():
    def __init__(self, name):
        self.name = name

    def method1(self):
        self.name = self.name.upper()
        print(self.name)

    l = [1]

    def method2(self, y):
        print(type(y))
        print(y.x)
        print(self.l)
        self.l.append(y)
        return self.l


a = A(10)
b = B('mike')
b.method1()
z = b.method2(a)
print(z)

# lists
ml = []
y_obj = {'a': [1, 2, 3],
         'b': [3, 4, 5]}
ml.append(y_obj)
print(ml)

# ********************** Sorting *******************************

# sort a list in python
l = ['anX', 'YaAaX', 'xyz', 'XaYZ', 'kaxyz', 'AX', 'Ax', 'A']

# default sort
l_sorted = sorted(l)
print(l_sorted)

# key sort, lower
l_sorted_key_lower = sorted(l, key=str.lower)
print(l_sorted_key_lower)

# key sort, upper
l_sorted_key_upper = sorted(l, key=str.upper)
print(l_sorted_key_upper)

# why is there no difference between lower and upper sorts?

y = sorted("This is a test string from Andrew".split(), key=str.lower)
print(y)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
# WOW...what is the differnce here?????


# sort a dictionary in python
people = {3: 'tom', 1: 'jeff', 2: 'Ted', 4: 'george'}
print(people)

# extract the key from people
for p in people:
    print(p)

# constuct the key, value tuples from people    
for p in people.items():
    print(p)

# default is to sort by key...constuct a list from the people dictionary
newl = sorted(people.items())
print(newl)

# now sort the people dictionary

# sort by key...default is dictionary key
people_sorted_by_key = dict(sorted(people.items()))
print(people_sorted_by_key)

# sort by value
people_sorted_by_value = dict(sorted(people.items(), \
                                     key=lambda item: item[1]))
print(people_sorted_by_value)

# ***************************** End Sorting ***************************

#  miscs
ml = ['a', 5, 'c', 'b']
ml.pop(2)
print(ml)

# enumerate
l = ['anX', 'YaAaX', 'xyz', 'XaYZ', 'kaxyz', 'A']
for idx, li in enumerate(l):
    print(idx, li)
    # j = idx
    for ll in li:
        if 'a' == ll:
            l.pop(0)
    print(l)

l = ['anX', 'YaAaX', 'xyz', 'XaYZ', 'kaxyz', 'A', 'A19', 'Eight', 'nine']
# construct a filter matrix that selects the 
l_filter = [True, True, False, False, True, True, True, False, False]
k = 0
for j, ll in enumerate(l_filter):
    print(j, ll)
    if ll == True:
        l.pop(j - k)
        k = k + 1
print(l)


# *********************************************
class Obj1:
    count = 100

    def __init__(self, name):
        self.name = name


class Obj2:
    count = 200

    def __init__(self, name):
        self.name = name


class Obj3:
    count = 300

    def __init__(self, name):
        self.name = name


obj1 = Obj1('one')
print(obj1.count)

obj2 = Obj2('two')
print(obj2.count)

obj3 = Obj3('three')
print(obj3.count)

objs = [obj2, obj1, obj3]
print(objs)
print('')
objs_sorted = sorted(objs, key=lambda x: x.count, reverse=False)
print(objs_sorted)

# continue and break statement
x = -3
while x <= 7:
    print((x, 4))
    x += 1
    if x == 5:
        continue
    print(f'x = {x}')


# a wee bit on decorators
def uppercase_decorator(function):
    def wrapper():
        func = function().upper()
        print(type(func))
        return func

    return wrapper


def howdy():
    return 'Howdy there, pardner'


howdy = uppercase_decorator(howdy)
howdy()


# but here is the shortcut, two_times method for doing this action

@uppercase_decorator
def say_hi():
    return 'hello there'


say_hi()


# a wee bit on functions
# note this won't work:
# def my_function:
#    return 'Thats all folks'
def my_function():
    return 'Thats all folks'


# setting a variable equal to function
m_func = my_function
print(type(m_func))  # this is a class 'function'
# evaluate the function
m_func()

# the right side of this equation evaluates the function, see ()
x = my_function()  # x is a class 'str'
print(type(x))
print(x)


# (1) a wee bit more on decorators
def test_decorator(function):
    # a function (wrapper) must be returned, not a string
    def wrapper():
        func = function().upper()
        return func

    # by returning the wrapper function, the decorated function is callable
    return wrapper


# (2) two_times

@test_decorator
def test_function():
    return 'Thats all folks'


print(f'test_function object original is {id(test_function)}')

# (3) function call
print(test_function())

# items 1, 2, and 3 are a shorthand for the following
# note, we will continue to use 1
test_function = test_decorator(test_function)
print(f'test_function object decorated is {id(test_function)}')
print(type(test_function))  # note, this is a class 'function' because we return the wrapper function
print(test_function())  # now call the function and get a class 'str'


# function as return value
def get_function():
    def print_it(s):
        print(s)

    return print_it


# use the function directly
get_function()('oooooo')

# set a function to a variable
p_func = get_function()
p_func('WoW')


# a wee bit about closure
def foo():
    x = 5

    def bar():
        print(x)

    return bar


func = foo()

print(func.__closure__)
print(type(func.__closure__))
print(len(func.__closure__))
print(func.__closure__[0].cell_contents)
func.__closure__[0].cell_contents

x_tuple = 2,
print(x_tuple)
print(len(x_tuple))
print(x_tuple[0])

y_tuple = (1, 2)
print(y_tuple)
print(len(y_tuple))
print(y_tuple[0])

# note how we can delete a variable associated with closure
# but closure will remember this variable
# closure
x = 'boy'


def foo(y):
    def bar():
        print(y)

    return bar


func = foo(x)
func()
del (x)
func()


# more on nested functions
def parent(arg1, arg2):
    value = 22
    my_dict = {'choc': 'yummy'}

    def child():
        print(2 * value)
        print(my_dict)
        print(arg1 + arg2)

    return child


new_function = parent(99, 1)
print([cell.cell_contents for cell in new_function.__closure__])


# WRITING FUNCTIONS IN PYTHONWhy does all of this matter?
# Decorators use:
# Functions as objects
# Nested functions
# Nonlocal scope
# Closures

# more on inheritance
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
    damage = 0  # note: here, damage will not give an exception...in creature

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
        damage = self.damage - enemy.armor
        if damage > enemy.hitpoints:
            damage = enemy.hitpoints
        enemy.hitpoints -= damage
        return damage

    def select_target(self, creatures):
        return creatures[0]

    def describe(self):
        return f'{self.name.capitalize()} the {self.__class__.__name__}'


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
        # print(sorted(creatures, key=lambda x: x.armor, reverse=False))
        creatures_worst_armor = \
            sorted(creatures, \
                   key=lambda x: x.armor, \
                   reverse=False)

        # determine if the list of creatures are only Orcs or HillOrcs
        length_creatures = len(creatures_worst_armor)
        orc_only_test = []
        for cwa in creatures_worst_armor:
            if isinstance(cwa, Orc) or isinstance(cwa, HillOrc):
                orc_only_test.append(True)
            else:
                orc_only_test.append(False)

        if sum(orc_only_test) == length_creatures \
                and creatures_worst_armor[0] != self:
            return creatures_worst_armor.pop(0)
        elif sum(orc_only_test) == length_creatures \
                and creatures_worst_armor[0] == self:
            return creatures_worst_armor.pop(1)

        # iterate on creatures according to rank        
        for c in creatures_worst_armor:
            if isinstance(c, Orc):  # note this will pass on c == self
                pass
            else:
                attacked = c
                return attacked


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
        if isinstance(enemy, Skeleton):
            damage = 0
            return damage

            # note how we have a local damage (damage) and a self.damage
        # associated with the instance object (e.g. Orc and Goblin)
        damage = self.damage - enemy.armor
        if damage > enemy.hitpoints:
            damage = enemy.hitpoints
        enemy.hitpoints -= damage
        return damage


class Skeleton(Creature):
    ''' Orc critter '''
    hitpoints = 8
    damage = 4
    armor = 0

    # Skeletons are more devious and opportunistic. They will choose the
    # creature in the list with the fewest hit points:
    def select_target(self, creatures):
        creatures_sorted = sorted(creatures, key=lambda x: x.hitpoints)
        for c in creatures_sorted:
            if c == self:
                pass
            else:
                attacked = c
                return attacked


orc1 = Orc('Orc1')
hillorc1 = HillOrc('HillOrc1')

# note that both Orcs and HillOrcs are Orc
print(isinstance(orc1, Orc))
print(isinstance(hillorc1, Orc))


# instance methods, class methods, and static methods
class TestClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


obj = TestClass()

# note that I could use the shortcut syntax:
# obj.method()

print(TestClass.instance_method(obj))

# note that I could use the shortcut syntax:
# obj.method()
print(obj.instance_method())

print(TestClass.class_method())

print(TestClass.static_method())

# list comprehensions
y = range(0, 21)
print(type(y))
xlist = [*y]
print(xlist)

xgen = (y for y in xlist)
print(type(xgen))
print([*xgen])

xcomp = [y for y in xlist]

xcomp2 = [y for y in xlist if y % 2 == 0]
xcomp3 = [y if y % 2 == 0 else 1 for y in xlist]

# more on list comprehensions
kilometer = [39.2, 36.5, 37.3, 37.8]
feet = [3280.839 * x for x in kilometer]
print(feet)

# change feet to integer values
feet_int = [int(x) for x in feet]
# capture only the uneven values of feet_int
uneven = [x % 2 for x in feet_int]
feet_int_uneven = [x if x % 2 else 0 for x in feet_int]

# sum the feet_int
feet_int_sum = sum([x for x in feet_int])


# Methods and Inheritance
class Pet:
    sound = ''

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.sound + '!'

    def describe(self):
        kind_of_pet = self.__class__.__name__.lower()
        return f'The {kind_of_pet} says: {self.speak()}'


class Dog(Pet):
    sound = 'woof'


class LapDog(Dog):
    sound = 'Yap'


class LoudLapDog(LapDog):
    # note that you need to comment out this sound to make super work properly
    # sound = 'YIP'
    def speak(self):
        return super().speak().upper() * 3


fido = Dog('Fido')
print(fido.describe())

chi = LapDog("Chi")
print(chi.describe())

cricket = LoudLapDog('Cricket')
print(cricket.describe())

# HTML
html_str = '''
    '<html><body>Welcome!</body></html>'
    '''
# first, return a copy of the string with leading and trailing characters removed
HOMEPAGE_HTML_MESSAGE = html_str.strip()
print(HOMEPAGE_HTML_MESSAGE)
print(type(HOMEPAGE_HTML_MESSAGE))
# given that BeautifulSoup is expecting a byte string, convert to said string
HOMEPAGE_HTML_MESSAGE = HOMEPAGE_HTML_MESSAGE.encode('ASCII')
print(type(HOMEPAGE_HTML_MESSAGE))

# use BeautifulSoup to parse and extract info from HOMEPAGE_HTML_MESSAGE
from bs4 import BeautifulSoup as bs4
import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
print(type(page))
print(type(page.content))
print(page.content)

soup = bs4(HOMEPAGE_HTML_MESSAGE, 'html.parser')
print(type(soup))

result = soup.find('body')
print(result)
print(result.prettify())
print(result.text)

# sorting a dictionary by key
mdict = {'c': 3, 'a': 1, 'e': 5, 'd': 4}
mdict_sorted = sorted(mdict.items())
print(mdict_sorted)


# more on classes
class ParentClass:
    def __init__(self):
        self.x_str = 'stringX'
        self.y_str = 'stringY'

    def my_tuple(self):
        ztuple = (self.x_str, self.y_str)
        # print(ztuple)
        return ztuple


class ChildClass(ParentClass):
    def my_tuple(self):
        print(self.x_str)
        return super().my_tuple() * 2


print_parent = ParentClass()
print_parent.my_tuple()

print_child = ChildClass()
print_child.my_tuple()


class ParentClass2:
    def __init__(self):
        self.x_str = 'stringX'
        self.y_str = 'stringY'

    def _xstring(self):
        return self.x_str

    def _ystring(self):
        return self.y_str

    def my_tuple(self):
        ztuple = self._xstring(), self._ystring()
        return ztuple


class ChildClass2(ParentClass2):
    def my_tuple(self):
        two_tuple = super().my_tuple() * 2
        return two_tuple


pclass = ChildClass2()
pclass.my_tuple()
pclass.x_str

# sentinal values

l = ['anX', 'YaAaX', 'xyz', 'XaYZ', 'kaxyz', 'A', 'A19', 'Eight', 'nine']
l_filter = [True, True, False, False, True, True, True, False, False]
test_dict = {d: e for d, e in zip(l, l_filter)}
print(test_dict)

# MISSING will be my sentinal value
MISSING = object()
key1 = "test"
val1 = test_dict.get(key1, MISSING)
key2 = "A"
val2 = test_dict.get(key2, MISSING)
if val1 is MISSING:
    print(f'key: "{key1}" is MISSING')
else:
    print(f'key1, "{key1}" is in dictionary, val={val1}')
if val2 is MISSING:
    print(f'key, "{key2}" is MISSING')
else:
    print(f'key, "{key2}" is in dictionary, val={val2}')
