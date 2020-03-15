dictionary1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
# dictionary1 = dict(key1='value1', key2='value2', key3='value3', key4='value4')

# creating entries in the dictionary

# print whole dictionary
print(dictionary1)

# print key and values
for key in dictionary1:
    print(key, dictionary1[key])

# another way to print key and values
for key, value in dictionary1.items():
    print(key, value)

# searching in dictionary
if 'key2x' in dictionary1:
    print('key found')
else:
    print('key not found')

# remove entry in dictionary1
dictionary1.pop('key4')
print(dictionary1)

print('---------------------------------------------------')
dictionary2 = dict()
dictionary2['key1a', 'key1b'] = ['value1a', 'value1b', 'value1c']
dictionary2['key2a', 'key2b'] = ['value2a', 'value2b', 'value2c']
print(dictionary2)
print(dictionary2['key1a', 'key1b'])

if ('key1a', 'key1b') in dictionary2:
    print('dictionary2 entry found')

movie_ratings = {
    'memento': 3,
    'primer': 3.5,
    'the_matrix': 5,
    'truman_show': 4,
    'red_dawn': 1.5,
    'skyfall': 4,
    'alex_cross': 2,
    'uhf': 1,
    'lion_king': 3.5
}

# dictionary comprehension
print({movie: rating for movie, rating in movie_ratings.items() if rating >= 4})
print({movie: movie_ratings[movie] for movie in movie_ratings if movie_ratings[movie] >= 4})

list1 = [(1, 2), (3, 4), (5, 6)]
print({tup[0]: tup[1] for tup in list1})

# d1 = dict(1 = 2, 3 = 4, 5 = 6)
d1 = dict(key1='value1', key2='value2', key3='value3', key4='value4')
print(tuple(d1))
print(tuple(d1.items()))
print(list(d1.items()))

d2 = {1: 2, 3: 4}
print(d2)
