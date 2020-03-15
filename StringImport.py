import string
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits, punctuation, \
    printable, whitespace

print('ascii_letters')
print(ascii_letters)
print('')

print('ascii_lowercase')
print(ascii_lowercase)
print('')

print('ascii_uppercase')
print(ascii_uppercase)
print('')

print('digits')
print(digits)
print('')

print('hexdigits')
print(hexdigits)
print('')

print('octdigits')
print(octdigits)
print('')

print('punctuation')
print(punctuation)
print('')

print('printable')
print(printable)
print('')

print('whitespace')
print(whitespace)
print('whitespace ordinal values: ', end='')
for c in whitespace:
    print(ord(c), end=' ')
print('\n')

# whitespace characters
#  9 - horizontal tab
# 10 - line feed
# 11 - vertical tab
# 12 - form feed
# 13 - carriage return
# 32 - space

for i in range(256):
    print('{:3d} - '.format(i), end='')
    if chr(i).isprintable():
        print(chr(i))
    else:
        print('not printable')
