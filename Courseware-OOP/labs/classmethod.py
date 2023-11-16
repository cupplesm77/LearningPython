# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:36:09 2023

I attempted to incorporate @classmethod for two use cases:
    1) alternate constructors, e.g. constructor_one and constructor_two
    2) changing class variables, e.g. change_default_age, etc.

Want to get a quick code review of my set of simple classes that apply classmethods.
Questions:

Do you consider the classes with classmethods as incorporating best practices?

Do you see interesting improvements needed for my class contrivances?

what about encapsulation?

What about my use of inheritance?

What about the Liskov Principle?

Using default class variables as method default parameter values?

"""

from dataclasses import dataclass, field


# ************************ ClassMethods ************************************
USE_DEFAULT_RANK = object()    # Sentinel Value usage
GLOBAL_RANK_DEFAULT = "First Lieutenant"
@dataclass
class Officer:
    name_default = "John Wayne"
    age_default = 37
    rank_default = "Colonel"
    """
        Toy classes illustrating application of best practices using @classmethod
    """
    name: str = field(default=name_default)
    age: int = field(default=age_default)
    rank: str = field(default=rank_default)

    @classmethod
    def constructor_one(cls, last_name=name_default, age=age_default, rank=rank_default):
        """
        Alternative constructor
        Parameters
            last_name: str   should use last name only for name
        """
        name = last_name
        return cls(name, age, rank)

    @classmethod
    def constructor_two(cls, name, rank):
        """
        An alternative constructor:
        A different interface than constructor_one and the baseclass interface
        Only includes name and rank call list parameters
        """
        return cls(name=name, rank=rank)   # note that the age is defaulted to officer age_default


class Marine(Officer):
    name_default = "Tony Curtis"
    age_default = 35
    rank_default = "Captain"

    @classmethod
    # def constructor_one(cls, name=name_default, rank=rank_default, age=age_default):  # Follow the Liskov Substitution Principle
    def constructor_one(cls, name=name_default, age=age_default, rank=USE_DEFAULT_RANK):
        if rank is USE_DEFAULT_RANK:
            rank = GLOBAL_RANK_DEFAULT
        else:
            rank = rank
        return cls(name, age, rank)

@dataclass
class Army(Officer):
    name_default = "Loyd Bridges"
    age_default = 31
    rank_default = "First Lieutenant"

    name: str = field(default=name_default)
    age: int = field(default=age_default)
    rank: str = field(default=rank_default)

    @classmethod
    def constructor_two(cls, name=name_default, rank=rank_default):  # note the implicit use of default age from officer
        return super().constructor_two(name, rank)

    @classmethod
    def constructor_three(cls, name=name_default, rank=rank_default):  # note the implicit use of default age
        return cls(name=name, rank=rank)


marine_officer0 = Marine.constructor_one()
print(marine_officer0.name)
print(marine_officer0.age)
print(marine_officer0.rank)

print("")
army_officer0 = Army.constructor_one()
print(army_officer0.name)
print(army_officer0.age)
print(army_officer0.rank)

print("")

officer1 = Marine.constructor_one("Cupples", 42)
print(officer1.name)
print(officer1.age)
print(officer1.rank)
officer1.age = 44
print(f"Officer1's revised age: {officer1.age}")

print("")
officer2 = Marine.constructor_one("Jones", 29, "Colonel")
print(officer2.name)
print(officer2.rank)
print(officer2.age)
print(f"officer2's current age: {officer2.age}")
print(f"Officer2's revised rank: {officer2.rank}")
print(f"Officer2's revised age: {officer2.age}")

print("")
officer3 = Army.constructor_two("Roger Stevens", "General")
print(f"officer3 is of type: {type(officer3)}")
print(f"officer3's name: {officer3.name}")
print(f"officer3's rank: {officer3.rank}")
print(f"officer3's age: {officer3.age}")

print("")
officer4 = Army.constructor_three("Timothy Cupples", "Colonel")
print(f"officer4 is of type: {type(officer4)}")
print(f"officer4's name: {officer4.name}")
print(f"officer4's rank: {officer4.rank}")
try:
    print(f"officer4's age: {officer4.age}")
except NameError:
    print("constructor_two does not have an age attribute")

# ************************ ClassMethods: END ************************************
