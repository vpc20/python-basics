# Sample dictionary
my_dict = {'banana': 3, 'apple': 4, 'orange': 2, 'mango': 1}

# Sorting by keys
sorted_by_keys = dict(sorted(my_dict.items()))
print("Original dictionary:", my_dict)
print("Sorted by keys:", sorted_by_keys)
print()

# ------------------------------------------------------------------------------

# Sample dictionary
my_dict = {'banana': 3, 'apple': 4, 'orange': 2, 'mango': 1}

# Sorting by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Original dictionary:", my_dict)
print("Sorted by values:", sorted_by_values)
print()

# ------------------------------------------------------------------------------

# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 3, 'grape': 1}

print("Original dictionary:", my_dict)
sorted_by_val_then_key = dict(sorted(my_dict.items(), key=lambda item: (item[1], item[0])))
print("Sorted by value and then by key:", sorted_by_val_then_key)
