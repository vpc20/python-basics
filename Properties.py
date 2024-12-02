class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Box:
    def __init__(self, weight):
        self.__weight = weight

    @property
    def weight(self):
        """Docstring for the 'weight' property"""
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self.__weight = weight

    @weight.deleter
    def weight(self):
        del self.__weight


me = Person("Alex")
print(me.name)
me.name = "Edward"
print(me.name)
