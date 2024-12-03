import random

first_name = "Jaya"
last_name = "Bodegard"


def print_variables():
    random_number = random.randint(0, 9)
    print(first_name)
    print(last_name)
    print(random_number)


global_variable = 'global'


def add(num1, num2):
    nested_value = 'Inside Function'
    print(num1 + num2)
    print(locals())


print(dir(__builtins__))
print(globals())
add(5, 10)
