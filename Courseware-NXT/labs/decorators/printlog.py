# printlog.py

# Some reasons to ue class-based decorators instead of functions:
# 1) To leverage inheritance or other OO features
# 2) To store state in the decorator as object attributes
# 3) You might believe that the class is more readable

# Also, use lower cass for the class name rather than the Uppercase that you would normally use for a class...
# because decorators are generally written as lower case names after the @ sign:  e.g.  @printlog not @PrintLog

"""
REMEMBER:
@printlog
def f_class(x):
    print(x + 2)

is shorthand for this:

def f_class(x):
    print(x + 2)
f_class = printlog(f_class)
Thus, we expect to pass the f_class function to the constructor...and therefore we need an __init__ in the class
that takes the func as an object
"""

class printlog:
    """
    The wrapped function is actually a printlog object
    """
    def __init__(self, func):
        self.func = func
    """
    The function being decorated is stored in the self.func ....
    Therefore, __call__ is in essence a wrapper function.
    """
    def __call__(self, *args, **kwargs):
        print(f"CALLING: {self.func.__name__}")
        return self.func(*args, **kwargs)


@printlog
def f_class(x):
    print(x + 2)

f_class(2)