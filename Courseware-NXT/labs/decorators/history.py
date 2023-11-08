# scratch_2.py
"""
Here are my questions and comments:
1) I understand the concept that a decorator has a "state"
2) I was taken by surprise when I saw how the parameter
VALUE (an integer in this case) could be set outside the scope
of wrapper and in the scope of history, YET a parameter
like y (an integer too...but it could have been another immutable)
was set the same way that VALUE was set, but could not be incremented
(changed) in the body of wrapper (y += 1).
Note how return_vals and x, which are not immutables, can be
changed in wrapper function.
"""
def history(func):
    return_vals = set()
    # ****** added for illustrative puposes
    VALUE = 10
    x = []
    y = 1
    # ******* end: added for illustrative purposes
    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        return_vals.add(return_val)
        print(f"Return values: {str(sorted(return_vals))}")
        # ******* Here is where the confusion lies *************************
        x.append("yes")
        # run next line commented out and not commented out
        y = y + return_val
        if VALUE >= 10:
             print(f"x = {x} and VALUE = {VALUE}")
             print(f"y = {y} and VALUE = {VALUE}")
        # ************** Here is where the confusion ends *******************
        return return_val, x, y

    return wrapper


@history
def foo(x):
    return x + 2


print(foo(3))
print(foo(1))
print(foo(4))
print(foo(1))
