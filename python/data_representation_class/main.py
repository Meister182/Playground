"""
Goal:
    * Have a class that has all the properties of a simple dict
    * when  class has no property returns None
"""


class DataClass:
    def _init_properties(self, d=None):
        """
        Initializes the class properties based on a dict.
        """
        if d is None:
            return None

        for key, value in d.items():
            setattr(self, key, value)

    def __getattr__(self, name):
        """
        When an atribute does not exist, return None instead of throwing an
        AtributeError.
        """
        # if name.isupper():
        #     return None
        # raise AttributeError(f"{self.__class__.__name__} as no attribute {name}")
        return None

    def get_dict(self):
        """ """
        properties = {}
        for name, value in vars(self).items():
            if name.startswith("_"):
                continue
            properties[name] = value
        return properties


class C(DataClass):
    def __init__(self, a="", d=None):
        self.a = a
        self._init_properties(d)
        self._protected = "foo"
        self.__private = "bar"


d = {"A": "foo", "B": "bar"}
cs = [C(), C("asd"), C(d=d)]

for c in cs:
    print(f"{c.__class__.__name__=}")
    print(f"{c.A=}")
    print(f"{c.B=}")
    print(f"{c.C=}")
    print(c.get_dict())
    print("-" * 10)
