# classmethod3.py
"""
Follow-up on prior question about using @classmethod
Revised question.

RE:  "It can modify a class state that would apply across all the instances of the class. For example, it can modify
a class variable that would be applicable to all instances."

See attachment with my toy example of what the above statement of class state and class variables.

Do you see my example as 1) being relevant to the above statement?
                                            2) does my example use best practices?

Note:  example extracted from a geeks for geeks example on related issue of alternate constructors...I expanded it
to include the issue of changing class variables.


"""


class EvalEquations:
    # an artificial class variable
    interesting_var = 1

    # basic constructor
    def __init__(self, a):
        self.ans = a

    # expression 1
    @classmethod
    def eq1(cls, args):
        # create an object for the class to return
        x = cls(((args[0] * args[0]) + (args[1] * args[1]) - args[2]) * cls.interesting_var)
        return x

    # expression 2
    @classmethod
    def eq2(cls, args):
        y = cls(((args[0] * args[0]) - (args[1] * args[1])) * cls.interesting_var)
        return y

    # expression 3
    @classmethod
    def eq3(cls, args):
        temp = 0

        # square of each element
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = cls(temp * cls.interesting_var)
        return z


print("")
eeq = EvalEquations([1, 2, 3])
print(f"type of class: {type(eeq)}")

print("")
print(f"EvalEquations Class Variable: 'interesting_var' is equal to {EvalEquations.interesting_var}")

li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
i = 0

# loop to get input three times
while i < 3:

    inp = li[i]

    # no.of.arguments = 2
    if len(inp) == 2:
        p = EvalEquations.eq2(inp)
        print(f"type of class: {type(p)}")
        print("equation 2 :", p.ans)

    # no.of.arguments = 3
    elif len(inp) == 3:
        q = EvalEquations.eq1(inp)
        print("equation 1 :", q.ans)

    # More than three arguments
    else:
        r = EvalEquations.eq3(inp)
        print("equation 3 :", r.ans)

    # increment loop
    i += 1

objs = [p, q, r]
for obj in objs:
    print(f"obj name: {obj}, ans: {obj.ans}, var: {obj.interesting_var}")
print("")
# ******** Here is where things get interesting from the standpoint of changing class variables *********
# Do you see this next set of code as using best practices????????

print("")
print("Change Eval Class Variable")
EvalEquations.interesting_var = 2
print(f"EvalEquations Class Variable: 'interesting_var' is now equal to {EvalEquations.interesting_var}")
print("")

# see how the interesting_var has been re-set to 2 in the objs already created....WOW
objs = [p, q, r]
for obj in objs:
    print(f"obj name: {obj}, ans: {obj.ans}, var: {obj.interesting_var}")
print("")

li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
i = 0
# loop to get input three times
while i < 3:

    inp = li[i]

    # no.of.arguments = 2
    if len(inp) == 2:
        t = EvalEquations.eq2(inp)
        print("equation 2 :", t.ans)

    # no.of.arguments = 3
    elif len(inp) == 3:
        u = EvalEquations.eq1(inp)
        print("equation 1 :", u.ans)

    # More than three arguments
    else:
        v = EvalEquations.eq3(inp)
        print("equation 3 :", v.ans)

    # increment loop
    i += 1

objs = [p, q, r, t, u, v]
for obj in objs:
    print(f"obj name: {obj}, ans: {obj.ans}, var: {obj.interesting_var}")
