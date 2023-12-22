# misc_exception.py

try:
    raise Exception("This is an error")
except Exception as e:
    print(e)
print("")
class MyException(Exception):
    pass

try:
    raise MyException("This is an error")
except Exception as e:
    print("MyException: {}".format(e))

print("")
# raise MyException("An error, as well")

class ErrorCodeException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
    def describe(self):
        return f"[{self.code}] {self.message}"
    def __str__(self):
        return self.describe()

try:
    raise ErrorCodeException("Alien Invasion Detected", 42)
except ErrorCodeException as err:
    print(err.describe())

class FileReadException(Exception):
    pass

class CorruptImageException(FileReadException):
    "Corrupt image exception"
    def __init__(self, image_path):
        self.path = image_path

class EarlyEndOfFileException(FileReadException):
    "truncated file exception"
    def __init__(self, file_path):
        self.path = file_path



def read_corrupt_image(image):
    raise CorruptImageException(image)

try:
    read_corrupt_image('secrets.jpg')
except FileReadException as file_error:
    print('{}: Bad file: '.format(file_error) + file_error.path)

try:
    read_corrupt_image('another_bad_image.jpg')
except CorruptImageException as file_error:
    print('Bad file: ' + file_error.path)


def read_truncated_file(file):
    raise EarlyEndOfFileException(file)


try:
    read_truncated_file('data.xls')
except FileReadException as file_error:
    print('Bad file: ' + file_error.path)

print("")

# These globals will be used by the send_money() function you write.
ACCOUNTS = {
    # name: amount in account
    'Jim': 20,
    'Stacy': 17,
    'Bob': 11,
    'Alice': 21,
}
# Add your country's currency to this list!
CURRENCIES = {'USD', 'CAN', 'EUR'}


class MoneyTransferError(Exception):
    "money transfer exception"
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
    def describe(self):
        return f"{self.sender} attempted to send {self.amount} to {self.recipient}"
    def __str__(self):
        return self.describe()


# >>> try:
# ...     send_money("Jim", "Tim", 42.75, "EUR")
# ... except MoneyTransferError as err:
# ...     print(err.describe_transfer())
# ...
# Jim attempted to send $42.75 to Tim


class MissingRecipientError(MoneyTransferError):
    "missing recipient exception"

class UnknownCurrencyError(MoneyTransferError):
    "unknown currency exception"

class InsufficientFundsError(MoneyTransferError):
    "insufficient funds exception"

class send_money(MoneyTransferError):
    def __init__(self, sender, recipient, amount, currency):

        if currency not in CURRENCIES:
            MoneyTransferError(sender, recipient, amount)
            raise UnknownCurrencyError('UnknownCurrencyError("{}")'.format(currency))

        if recipient not in ACCOUNTS:
            MoneyTransferError(sender, recipient, amount)
            raise MissingRecipientError("${:.2f}: {} -> {} ".format(amount, sender, recipient))
        #         MissingRecipientError: $42.75: Jim -> Tim

        if amount > ACCOUNTS[sender]:
            MoneyTransferError(sender, recipient, amount)
            raise InsufficientFundsError('${:.2f}: {} -> {}'.format(amount, sender, recipient))

        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.denomination = currency


        ACCOUNTS[self.sender] -= self.amount
        ACCOUNTS[self.recipient]  += self.amount
        message = "Successfully transferred ${:.2f} from {} to {}"
        print(message.format(self.amount,
                             self.sender,
                            self.recipient
                            )
              )

send_money("Jim", "Bob", 14.5, "USD")
# Successfully transferred $14.50 from Jim to Bob
send_money("Bob", "Alice", 21.25, "USD")
# Successfully transferred $21.25 from Bob to Alice

try:
    send_money("Jim", "Tim", 42.75, "EUR")
except MoneyTransferError as err:
    print(err.describe_transfer())
# Jim attempted to send $42.75 to Tim