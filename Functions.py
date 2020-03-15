print(abs(-123))  # 123

print(any([True, True, True]))  # True
print(any([True, False, False]))  # True
print(any([False, False, False]))  # False

print(all([True, True, True]))  # True
print(all([True, False, False]))  # False
print(all([False, False, False]))  # False

print(chr(65))  # 'A'
print(chr(90))  # 'Z'
print(chr(97))  # 'a'
print(chr(122))  # 'z'

print(len(''))  # 0
print(len('abcde'))  # 5

print(len([]))  # 0
print(len([1, 2, 3]))  # 3

print(min(['aaa', 'bb', 'c']))
print(min(['aaa', 'bb', 'c'], key=len))

print(max(['aaa', 'bb', 'c']))
print(max(['aaa', 'bb', 'c'], key=len))

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122

print(list(range(0)))  # []
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list(range(2, 11, 2)))  # [2, 4, 6, 8, 10]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

print(list(range(5, 51, 5)))  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(sorted(['aaa', 'b', 'cc']))
print(sorted(['aaa', 'b', 'cc'], key=len))
print(sorted(['aaa', 'b', 'cc'], reverse=True))
print(sorted(['aaa', 'b', 'cc'], key=len, reverse=True))

print(sum([1, 2, 3]))  # 6




















