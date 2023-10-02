# person.py
from dataclasses import dataclass


@dataclass
class Person:
    first: str
    last: str

    def full_name(self):
        full = f'{self.first} {self.last}'
        return full

    def formal_name(self, salutation):
        formal = f'{salutation}. {self.first} {self.last}'
        return formal

# guy = Person("John", "Doe")
# self.assertEqual("John", guy.first)
# self.assertEqual("Doe", guy.last)
# self.assertEqual("John Doe", guy.full_name())
# self.assertEqual("Mr. John Doe", guy.formal_name())
