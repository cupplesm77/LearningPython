'''

Let's create a class to manage invoices. Its constructor will take
an invoice number, the customer name, and the amount of money owed.

>>> invoice = Invoice(12, 'Mark Smith', 42.50)
>>> invoice.number
12
>>> invoice.customer
'Mark Smith'
>>> invoice.amount
42.5

And we'll keep track too of the total payments made. At first, this
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

Sometimes, a customer will submit one large payment for several
invoices. And it may only partially cover one of them. Create a
CustomerAccount class to manage the nuances of this.

>>> customer_name = 'James Jones'
>>> account = CustomerAccount(customer_name)

Did you know Python class objects have a __name__ attribute?
>>> type(account).__name__
'CustomerAccount'
>>> account.name
'James Jones'

The add_invoice() method takes an instance of the Invoice class.

>>> account.add_invoice(Invoice(1, customer_name, 20.0))
>>> len(account.invoices)
1
>>> account.total_due()
20.0
>>> account.add_invoice(Invoice(2, customer_name, 25.0))
>>> len(account.invoices)
2
>>> account.total_due()
45.0
>>> account.add_invoice(Invoice(3, customer_name, 30.0))
>>> len(account.invoices)
3
>>> account.total_due()
75.0

>>> unpaid = account.unpaid_invoices()
>>> len(unpaid)
3
>>> type(unpaid[0]).__name__
'Invoice'
>>> unpaid[0].number
1
>>> unpaid[0].amount
20.0

>>> account.apply_payment(20)
>>> now_unpaid = account.unpaid_invoices()
>>> len(now_unpaid)
2
>>> now_unpaid[0].number
2
>>> account.total_due()
55.0

>>> account.apply_payment(10)
>>> account.total_due()
45.0
>>> len(account.unpaid_invoices())
2

>>> account.apply_payment(45)
>>> len(account.unpaid_invoices())
0

'''

# Write your code here:
class Invoice():
    ''' invoice class 
    '''
    def __init__(self, invoice_num, name, owed):
        self.number = invoice_num
        self.customer = name
        self.amount = owed
        self.total_payments = 0
        
    
    def add_payment(self, payment):
        self.total_payments = self.total_payments + payment
        
    def is_fully_paid(self):
        if self.total_payments == self.amount:
            return True
        else:
            return False
        
    def amount_due(self):        
        return self.amount - self.total_payments

class CustomerAccount():
    ''' manage customer invoices and other matters 
    '''
    def __init__(self, name):
        self.name = name
        self.invoices = []
        self.due = 0.0
        self.excess_payment = 0.0
        
    def add_invoice(self, y):
        ''' add an invoice for customer '''       
        self.invoices.append(y)
        #print(self.invoices)
    
    def total_due(self):
        total_owed = 0
        for invoice in self.invoices:
            total_owed = total_owed + invoice.amount_due()
        self.due = total_owed
        return self.due
    
    def unpaid_invoices(self):
        ''' provide the number of unpaid invoices  '''
        return self.invoices
    
    def apply_payment(self, payment):
        ''' apply a payment toward an unpaid balance '''
        remaining_payment = 0
        first_time = True
        for invoice in self.invoices:
            ''' iterate over the existing invoices '''
            # setup logic for multiple passes over invoices
            if remaining_payment == 0 and first_time:
                payment = payment
                first_time = False
            elif remaining_payment > 0:
                # break from for loop if the remaining payment = 09
                payment = remaining_payment
            else:
                # break from the invoice loop if the remaining_payment=0
                break
            #             
            # initialize amount owed
            owed = invoice.amount_due()
            if payment < owed:
                pay = payment
                invoice.add_payment(pay)
                remaining_payment = 0
            elif payment == owed:
                pay = owed
                invoice.add_payment(pay)  
                remaining_payment = 0
            else:
                pay = owed
                invoice.add_payment(pay)  
                remaining_payment = payment - owed

        # construct a filter matrix that selects the components 
        # of invoices to remove if the invoice is fully paid
        current_invoices = self.invoices
        invoice_filter = [invc.is_fully_paid() for invc in current_invoices]
        self._remove_invoice(invoice_filter)
                
        if remaining_payment > 0:
            self.excess_payment = remaining_payment                        
                 
    def _remove_invoice(self, invoice_filter):
        ''' if invoice has been paid, remove from unpaid_invoices '''
        k = 0
        for j, ll in enumerate(invoice_filter):
            #print(j, ll)
            if ll == True:
                self.invoices.pop(j-k)
                k=k+1
       


invoice = Invoice(12, 'Mark Smith', 42.50)
print(invoice.number)
print(invoice.customer)
print(invoice.amount)
print(invoice.total_payments)
invoice.add_payment(20)
print(invoice.is_fully_paid())
print(invoice.total_payments)
print(invoice.amount_due())

customer_name = 'James Jones'
account = CustomerAccount(customer_name)
print(type(account).__name__)
print(account.name)
account.add_invoice(Invoice(1, customer_name, 20.0))
print(len(account.invoices))
print(account.total_due())
account.add_invoice(Invoice(2, customer_name, 25.0))
print(len(account.invoices))
print(account.total_due())
account.add_invoice(Invoice(3, customer_name, 30.0))
print(len(account.invoices))
print(account.total_due())


unpaid = account.unpaid_invoices()
print(len(unpaid))
print(type(unpaid[0]).__name__)
print(unpaid[0].number)
print(unpaid[0].amount)


account.apply_payment(20)
now_unpaid = account.unpaid_invoices()
print(len(now_unpaid))
print(now_unpaid[0].number)
print(unpaid[0].amount)
print(account.total_due())

account.apply_payment(10)
print(account.total_due())
print(len(account.unpaid_invoices()))

account.apply_payment(45)
print(len(account.unpaid_invoices()))


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
