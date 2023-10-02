# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:59:04 2023

Practice 1 for Powerful Python

@author: gravi
"""

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def full_name(self):
        return self.first + " " + self.last
    def formal_name(self, title):
        return title + " " + self.full_name()
    
person = Person('Mike', 'Cupples')
print(person.formal_name('Mr.'))


