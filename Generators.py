
# x = range(10)
# print x
# print type(x)

def number_generator(n):
    for i in range(n):
        yield i

for num in number_generator(10):
    print(num)

# generator comprehension
animals = ['dog', 'cat', 'duck']
for a in  (animal for animal in animals):
    print(a)