'''Create a class representing a concert ticket.
Its constructor takes two values: a ticket price,
and a section.

>>> my_ticket = ConcertTicket(22.0, 'floor')
>>> your_ticket = ConcertTicket(42.0, 'mezzanine')

You can access these two values through the price and section
attributes:

>>> my_ticket.price
22.0
>>> your_ticket.section
'mezzanine'

Once set, the price cannot be changed. If you try to set it,
it raises an error.

>>> my_ticket.price = 20.0
Traceback (most recent call last):
...
AttributeError: can't set attribute 'price'

The section can be changed, but can only be set to "floor", "lower",
"mezzanine", or "premier". If you try to change it to something
different, a ValueError is raised, with a descriptive error message:

>>> my_ticket.section = "lower"
>>> my_ticket.section
'lower'
>>> my_ticket.section = "premier"
>>> my_ticket.section
'premier'
>>> my_ticket.section = "upper_mezzanine"
Traceback (most recent call last):
...
ValueError: Invalid section "upper_mezzanine"

'''

# Write your code here:
class ConcertTicket:
    SECTION = {"floor", 
               "lower",
               "mezzanine", 
               "premier"}
    def __init__(self, price, section):
        self._price = price
        # note, you are calling the section setter with this line:
        self.section = section   # calling section setter for validation.
        
    @property 
    def price(self):
        return self._price
    
    @property 
    def section(self):
        return self._section
    
    @section.setter 
    def section(self, value):
        ''' perform validation of value at initialization
        and at subsequent settings
        '''
        if value not in self.SECTION:
            raise ValueError(f'{value} not a valid section')
        self._section = value
            
my_ticket = ConcertTicket(22.0, 'floor')
your_ticket = ConcertTicket(42.0, 'mezzanine')

print(my_ticket.price)
# 22.0
print(your_ticket.section)
# 'mezzanine'

# Once set, the price cannot be changed. If you try to set it,
# it raises an error.
# try:
#     my_ticket.price = 20.0
#     print(my_ticket.price)
# except AttributeError as error:
#     print(f"{error}: can't set ticket price")


# The section can be changed, but can only be set to "floor", "lower",
# "mezzanine", or "premier". If you try to change it to something
# different, a ValueError is raised, with a descriptive error message:

my_ticket.section = "lower"
print(my_ticket.section)

# my_ticket.section = "premier"
# print(my_ticket.section)
#'premier'
# my_ticket.section = "upper_mezzanine"
#Traceback (most recent call last):
#...
# ValueError: Invalid section "upper_mezzanine"

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
