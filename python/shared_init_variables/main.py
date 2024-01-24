# WRONG WAY OF DOING THIS:
#
# Since bs is initialized with a list in the constructor,
# the list variable WILL BE SHARED BY ALL INSTANCES!!
class A():
    def __init__(self, bs = []):
        self._bs = bs 

    def add_b(self, b):
        self._bs.append(b)

a1 = A()
a1.add_b("b1")

a2 = A()
a2.add_b("b2")

a3 = A()
a3.add_b("b3")

print("WRONG: ", a2._bs)


# Proper WAY OF DOING THIS:
#
# Since bs is initialized with a list in the constructor,
# the list variable WILL BE SHARED BY ALL INSTANCES!!
class A():
    def __init__(self, bs = []):
        self._bs = list(bs) # Creates a copy of the default bs variable

    def add_b(self, b):
        self._bs.append(b)

a1 = A()
a1.add_b("b1")

a2 = A()
a2.add_b("b2")

a3 = A()
a3.add_b("b3")

print("Correct: ", a2._bs)

