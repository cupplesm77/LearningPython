# misc.py
def pv(u):
    print(u)

(lambda: pv(10))()


z = lambda: pv(101)
z()

