from collections import defaultdict

g = {'s': {'t': 10, 'y': 5},
     't': {'x': 1, 'y': 2}}

# accessing value
print(g['s']['t'])

# adding another value
g['s']['z'] = 9
print(g)


# creating nested dictionary
g = dict()
g['s'] = dict()
g['s']['t'] = 10
g['s']['y'] = 5
g['t'] = dict()
g['t']['x'] = 1
g['t']['y'] = 2
print(g)


# creating nested dictionary - simpler if defaultdict is used
g = defaultdict(dict)
g['s']['t'] = 10
g['s']['y'] = 5
g['t']['x'] = 1
g['t']['y'] = 2
print(g)

