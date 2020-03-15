print('abcdefghijklmnopqrstuvwxyz'.upper())
print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
print('pYTHON'.capitalize())
print('structure and interpretation of computer programs'.title())
print('sTRING sWAPCASE'.swapcase())

print('     String with leading spaces'.lstrip())
print('#####String with leading hashtag'.lstrip('#'))
print('String with trailing spaces     '.rstrip())
print('String with trailing hashtag #####'.rstrip('#'))
print('     String with leading and trailing spaces     '.strip())
print('#####String with leading and trailing hashtag#####'.strip('#'))

print('Centered Title'.center(80, '='))
print('   Left-justified Title'.strip().ljust(80, '<'))
print('Right-justified Title'.rjust(80, '>'))

print('sort-bubble.txt'.startswith('sort'))
print('file1.txt'.endswith('txt'))

print('\tabcdefghijklmnopqrstuvwxyz'.expandtabs(25))

print('i am what i am'.count('am'))

print('/'.join(['a', 'b', 'c']))
print(''.join(['a', 'b', 'c']))

print('Spam and Eggs and Spam'.replace('Spam', 'Eggs'))
print('Spam and Eggs and Spam'.replace('Spam', 'Eggs', 1))

print('the/quick/brown/fox'.split('/'))
print('the/quick/brown/fox'.split('/', 1))
print('the/quick/brown/fox'.split('/', 2))
print('the/quick/brown/fox'.split('/', 3))

print('the quick brown fox'.rsplit(' '))
print('the quick brown fox'.rsplit(' ', 1))
print('the quick brown fox'.rsplit(' ', 2))
print('the quick brown fox'.rsplit(' ', 3))

print('i am what i am'.index('am'))  # raises ValueError when string is not found
print('i am what i am'.rindex('am'))  # raises ValueError when string is not found

print('i am what i am'.find('am'))  # returns -1 when string is not found
print('i am what i am'.rfind('am'))  # returns -1 when string is not found

print('123'.zfill(5))

print('Sample string for / the partition method'.partition('/'))
print('C:\\Users\Victor Cuevas\PycharmProjects\PythonBasics'.rpartition('\\'))

s = ''' Sample text
spread out in
several lines'''
print(s.splitlines())

# from string import maketrans
s = "this is string example....wow!!!"
print(s.maketrans("aeiou", "12345"))
print(s.translate(s.maketrans("aeiou", "12345")))

s = 'remove vowels'
# print(s.translate(s.maketrans(dict(a='', e='', i='', o='', u=''))))
print(s.translate(s.maketrans('', '', 'aeiou')))

s = 'abc'
print(s.translate(s.maketrans(dict(a='zz', b='yy', c='xx'))))

