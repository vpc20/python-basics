a = [1, 2, 3]
b = [4, 5, 6]

zipped = list(zip(a, b))
print(zipped)

# sum_list = []
# for zip_item in zipped:
#     sum_list.append(sum(zip_item))
# print sum_list

print([sum(zip_item) for zip_item in zipped])
