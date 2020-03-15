list1 = ['Python', 'Ruby', 'Java']

print('original list - ', list1)

list1.reverse()
print('list1.reverse() - ', list1)

list1.sort()
print('list1.sort() - ', list1)

list1.extend(['C', 'COBOL'])
print('list1.extend(["C", "COBOL"]) - ', list1)

list1.append('Javascript')
print('list1.append("Javascript") - ', list1)

list1.insert(3, "Erlang")
print('list1.insert(3, "Erlang") - ', list1)

list1.pop(3)
print('list1.pop(3) - ', list1)

list1.remove('COBOL')
print('list1.remove("COBOL") - ', list1)

print('list1.index("Python") - ', list1.index('Python'))
print('list1.count("Java") - ', list1.count("Java"))

list1 = ['cc', 'aa', 'bb', 'c', 'b', 'a', ]
list1.sort(key=lambda e: (len(e)))
print(list1)
list1.sort(key=lambda e: (len(e), e))
print(list1)

list1 = [('a1', 0, 4), ('a3', 9, 12), ('a2', 5, 8)]
list1.sort(key=lambda e: e[2])
print(list1)

