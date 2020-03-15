s1 = 'abcdefghij'

i = 0
while i < len(s1):
    print(s1[i], end=' ')
    i += 1

print(' ')

i = len(s1)
while i > 0:
    i -= 1
    print(s1[i], end=' ')

