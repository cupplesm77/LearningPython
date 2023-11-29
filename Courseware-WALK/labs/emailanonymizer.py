'''

>>> anonymize = EmailAnonymizer()

>>> anonymize('bob@powerfulpython.com')
'anon0@powerfulpython.com'

>>> anonymize('jane@powerfulpython.com')
'anon1@powerfulpython.com'

>>> anonymize('bob@powerfulpython.com')
'anon0@powerfulpython.com'

>>> anonymize('tom@powerfulpython.com')
'anon2@powerfulpython.com'

>>> anonymize('jane@powerfulpython.com')
'anon1@powerfulpython.com'

'''

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
