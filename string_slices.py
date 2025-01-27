
string1 = 'abcde'

print('first char')
print(string1[0])

print('last char')
print(string1[-1])

print('head')
print(string1[0:1])

print('tail')
print(string1[1:])
# print(string1[1:len(string1)])

print('leading chars (exclude last char)')
print(string1[:-1])
# print(string1[0:len(string1)-1])

print('first 3 char')
print(string1[:3])

print('last 3 char')
print(string1[-3:])
# print(string1[len(string1)-3:])

print('exclude first and last character')
print(string1[1:-1])

print('reverse string')
print(string1[::-1])
