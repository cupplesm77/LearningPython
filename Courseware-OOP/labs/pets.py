# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:22:57 2023

@author: gravi
"""

class Pet:
    pet_type = ''
    sound = ''
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f' the {self.pet_type} says: {self.sound}'
        
class Dog(Pet):
    pet_type = 'dog'
    sound = 'Wolf!'
    
class Cat(Pet):
    pet_type = 'cat'
    sound = 'Meow!'
    
fred = Dog('Fred')    
misha = Cat('Misha')
print(fred.name + ' ' + fred.describe())
print(misha.name + ' ' + misha.describe())