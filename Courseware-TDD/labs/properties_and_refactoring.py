# Money Class


# class Money:
#     def __int__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents


# refactor  Money to change internal usage to total_cents rather than dollars and cents
# maintain external interface by using properties
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        """provides the total number of whole dollars in total cents"""
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        """new_dollars (>= 0) new value of dollars in whole dollars, e.g. 1, 2, 10, 45, etc. dollars"""
        self.total_cents = new_dollars * 100 + self.cents

    @property
    def cents(self):
        """provides the cents portion of the total cents"""
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        """new_cents (>=0) is new value in cents in total cents , e.g. 20, 120, 99 or 921, etc. cents"""
        self.total_cents = self.dollars * 100 + new_cents


# prove Money class functions as expected
money = Money(1, 23)
print(money.cents)
print(money.dollars)
print("")
money.cents = 10
print(money.cents)
print(money.dollars)
print("")
money.dollars = 2
print(money.cents)
print(money.dollars)
print("")
money.cents = 187
print(money.cents)
print(money.dollars)
print("")
print("**********************************************************")
print("")


class OtherGuysClass(Money):
    def set_new_dollars(self, new_dollars):
        self.dollars = new_dollars * 5
        return self.dollars

    def set_new_cents(self, new_cents):
        self.cents = new_cents * 10
        return self.cents


ogc = OtherGuysClass(100, 10)
print(ogc.cents)
print(ogc.dollars)
print("")
ogc.set_new_cents(2)
ogc.set_new_dollars(4)
print(ogc.cents)
print(ogc.dollars)
