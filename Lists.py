# joining lists
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]

joined_list = list1 + list2 + list3
print(joined_list)


# flatten a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]

flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)


# flatten a list of lists which contains more lists
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            for i in flatten(item):
                yield i
        else:
            yield item


def flatten1(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            for i in flatten(item):
                flat_list.append(i)
        else:
            flat_list.append(item)
    return flat_list


list_of_lists = [[1, 2], [3, 4], [5, 6, [7, 8]], 9]

for x in flatten(list_of_lists):
    print(x)

print(flatten1(list_of_lists))


# convert string to list of characters
string = 'abcde'
ch_list = [ch for ch in string]
print(ch_list)


# convert list of characters to string
list1 = ['a', 'b', 'c', 'd', 'e']
string = ''.join(ch for ch in list1)
print(string)


# sort characters in string
string = 'cedba'
ch_list = [ch for ch in string]  # convert string to list of characters
sorted_ch_list = sorted(ch_list)  # sort the list of characters
ch_list = ''.join(ch for ch in sorted_ch_list)  # convert the list of characters to string
print(ch_list)
# print ''.join(ch for ch in (sorted([ch for ch in string])))


# remove duplicates in list
list1 = ['ab', 'cd', 'ab', 'cd']
list2 = list(set(list1))
print(list2)
