'''

Let's create a class to manage invoices. Its constructor will take
an invoice number, the customer name, and the amount of money owed.

>>> invoice = Invoice(12, 'Mark Smith', 42.50)

The built-in isinstance() tells you whether an object is an instance of
a given class or not.
>>> isinstance(invoice, Invoice)
True

This object has some member variables:
>>> invoice.number
12
>>> invoice.customer
'Mark Smith'
>>> invoice.amount
42.5

We want to keep track too of the total payments made. At first, this
will be zero.

>>> invoice.total_payments
0

Now, the customer may make payments in stages (rather than paying all
at once).  So let's create methods to add payments, check whether the
invoice is fully paid off, etc.

>>> invoice.add_payment(20)
>>> invoice.is_fully_paid()
False
>>> invoice.total_payments
20
>>> invoice.amount_due()
22.5

>>> invoice.add_payment(22.50)
>>> invoice.is_fully_paid()
True
>>> invoice.amount_due()
0.0

'''

# Write your code here:
class Invoice():
    ''' invoice class 
    '''
    def __init__(self, invoice_num, name, owed):
        self.number = invoice_num
        self.customer = name
        self.amount = owed
        
    total_payments = 0
    
    def add_payment(self, payment):
        self.total_payments = self.total_payments + payment
        
    def is_fully_paid(self):
        if self.total_payments == self.amount:
            return True
        else:
            return False
        
    def amount_due(self):        
        return self.amount - self.total_payments

invoice = Invoice(12, 'Mark Smith', 42.50)
print(invoice.number)
print(invoice.customer)
print(invoice.amount)
print(invoice.total_payments)
invoice.add_payment(20)
print(invoice.is_fully_paid())
print(invoice.total_payments)
print(invoice.amount_due())

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
