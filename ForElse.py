list1 = [1, 2, 3, 4, 5]


# without for-else construct
# def find_number(n):
#     number_found = False
#     for num in list1:
#         if num == n:
#             number_found = True
#             break
#
#     if number_found:
#         print 'Number {:,} is found'.format(n)
#     else:
#         print 'Number {:,} is not found'.format(n)

# using for-else construct
def find_number(lst, n):
    list1 = lst
    for num in list1:
        if num == n:
            print('Number {:,} is found'.format(n))
            break
    else:
        print('Number {:,} is not found'.format(n))


find_number(list1, 3)
find_number(list1, 10)
