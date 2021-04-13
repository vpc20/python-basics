# x = range(10)
# print x
# print type(x)

def number_generator(n):
    for i in range(n):
        yield i


gennum = number_generator(10)
print(next(gennum))
print(next(gennum))
print(next(gennum))

# print the rest
for num in gennum:
    print(num)

# generator comprehension
animals = ['dog', 'cat', 'duck']
for a in (animal for animal in animals):
    print(a)
