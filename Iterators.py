class InfiniteCounter:

    def __init__(self):
        self.ctr = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.ctr += 1
        return self.ctr


# create an object
infctr = InfiniteCounter()

# create an iterable from the object
ic = iter(infctr)

# Using next to get to the next iterator element
print(next(ic))
print(next(ic))
print(next(ic))
print(next(ic))
print(next(ic))


# create iterator from sequence
iter1 = iter([1, 2, 3, 4, 5])

print(next(iter1))
print(next(iter1))
for e in iter1:
    print(e)
