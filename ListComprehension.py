list1 = ['a', 'b', 'c', 'd', 'e']

print([i for i in range(len(list1))])
print([ch for ch in list1])

print([i for i, ch in enumerate(list1)])
print([ch for i, ch in enumerate(list1)])
print([[i, ch] for i, ch in enumerate(list1)])

print([i for i in range(10) if i % 2 == 0])
print([i if i % 2 == 0 else 'odd' for i in range(10)])

print([[i, j] for i in range(8) for j in range(8)])

