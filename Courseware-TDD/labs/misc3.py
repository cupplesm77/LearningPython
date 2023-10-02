# misc3 is for practice and experimenting with python

# from dataclasses import dataclass, field, KW_ONLY
from dataclasses import dataclass, field
import pandas as pd
from collections import defaultdict

# Support for type hints
from typing import Any

d = defaultdict(defaultdict)
d[1][2] = "'That's all folks"
print(d)
d[1] = "ONE"
print(d)
d[2] = "two"
print(d)


def new_d():
    return defaultdict(new_d)


a = defaultdict(new_d)
print(a)
a[1] = "ONE"
print(a)
a[2] = "two"
print(a)
a[3] = "three"
print(a)

d = defaultdict(new_d)
d[2][3][4][5][6] = "this works"
print(d)


@dataclass
class CSVDataReader:
    """
    Baseclass
    """

    name: str
    df: pd.DataFrame = field(default_factory=pd.DataFrame)

    @classmethod
    def from_csv(cls, name, path_to_csv, **df_options):
        return cls(name, pd.read_csv(path_to_csv, **df_options))

    def print_df(self):
        print(f"{self.name} Account Data = \n{self.df}")


class BankAccountReader(CSVDataReader):
    num = 1

    @classmethod
    def from_csv(cls, name, path):
        return super().from_csv(name, path, skiprows=cls.num)


class CreditCardReader(CSVDataReader):
    column_names = ["Date", "Description", "Category", ...]

    @classmethod
    def from_csv(cls, name, path):
        return super().from_csv(name, path, names=cls.column_names)


input_file_path = "test.csv"

bank = BankAccountReader("Bank")
print(bank.name)
credit = CreditCardReader("Credit Card")
print(credit.name)

df_bank = bank.from_csv(bank.name, input_file_path)
print(type(df_bank.df))
df_bank.print_df()
print("")

df_credit = credit.from_csv(credit.name, input_file_path)
print(type(df_credit.df))
df_credit.print_df()


# examples of dataclasses

# The Any type
# A special kind of type is Any. A static type checker will treat every type as being compatible with Any
# and Any as being compatible with every type.
# This means that it is possible to perform any operation or method call on a value of type Any and
# assign it to any variable:


@dataclass
class Base:
    x: Any
    # _: KW_ONLY
    y: int = 0
    w: int = 1


@dataclass
class D(Base):
    z: float = 10
    # t: int = field(kw_only=True, default=0)
    t: int = field(default=0)


# Any is a string
d_str = D("any", y=1, w=99, z=77.98, t=1000000)
# Any is an int
d_int = D(11, y=1, w=99, z=77.98, t=1000000)
# Any is a float
d_float = D(17.1135, y=1, w=99, z=77.98, t=1000000)
# Any is a bool
d_bool = D(True, y=1, w=99, z=77.98, t=1000000)
# Any is an object
d_object = D(object(), y=1, w=99, z=77.98, t=1000000)

print(d_str.x)
print(d_int.x)
print(d_float.x)
print(d_bool.x)
print(d_object.x)

# list oddity
SECTIONS = [
    "First",
    "Second",
    "Third",
]
print(type(SECTIONS))
print(SECTIONS)

# string parsing: count number of paragraphs

string0 = ""

string1 = """This is a one paragraph string

"""

string3 = """This is a rather short story. It has three paragraphs.

Once upon a time, a brave princess went on a dangerous journey. She
had many adventures, and recruited other heroes to her important and
noble cause.

She prevailed, saving the day, and made it home. Yay!"""

test_split = string1.split("\n\n")
print(test_split)
num_paragraphs = len(test_split)
print(num_paragraphs)

thecount = string3.count("\n\n")
num_paragraphs = thecount + 1
print(num_paragraphs)
