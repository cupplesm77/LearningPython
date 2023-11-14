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
