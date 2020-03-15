import random


class Dice:
    @staticmethod
    def roll():
        return random.choice((1, 2, 3, 4, 5, 6))


d1 = Dice()
d2 = Dice()
print("Dice 1 : ", d1.roll())
print("Dice 2 : ", d2.roll())

print('Random range 0-9: ', random.randrange(10))

lst = [1, 2, 3]
random.shuffle(lst)
print('Random shuffle :', lst)
