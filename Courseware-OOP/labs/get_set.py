# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:51:55 2023

Python Properties

getset.py

python getters and setters

@author: gravi
"""

# getters and setter in python
class Person:
    ''' Person class illustrating python
    getter and setter Properties
    '''
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property  
    def full_name(self):
        return self.first + ' ' + self.last
    
    @full_name.setter 
    def full_name(self, value):
        first, last = value.split(' ')
        self.first = first
        self.last = last
    
person = Person('Joe', 'Thomas')    
print(person.full_name)
thename = person.full_name
print(f'name is {thename}')
person.full_name = "Joseph Jeffries"
print(person.full_name)
  

class Ticket:
    def __init__(self, price):
        ''' see the validation in this line: self.price invokes 
        # the setter price method, setting self._price AND
        validating that the price is always >= 0 when set.
        '''
        self.price = price  # **** see trick here *****
    @property 
    def price(self):
        return self._price
    @price.setter 
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('Nice Try')
        self._price = new_price

print('')
ticket1 = Ticket(1.25)
print(f'The ticket1 price is {ticket1.price}')
print('')

# ticket2 = Ticket(-1.25)
# print(f'The ticket2 price is {ticket2.price}')

# other tests/trials etc

class ConcertTicket:
    def __init__(self, price, section):
        self._price = price
        self._section = section
        
    @property 
    def price(self):
        return self._price    
    @property 
    def section(self):
        return self._section    
    
    
    
my_ticket = ConcertTicket(22.0, 'floor')
your_ticket = ConcertTicket(42.0, 'mezzanine')
print(my_ticket.price)
#22.0
print(your_ticket.section)
#'mezzanine'
try:
    my_ticket.price = 20.0
except AttributeError as error:
    print(f'{error}: ticket price is read-only')

