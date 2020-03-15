# a --> z
# b --> y
# c --> x

from string import ascii_lowercase

print(ascii_lowercase)


def simple_encrypt(s):
    return s.translate(s.maketrans(ascii_lowercase, ascii_lowercase[::-1]))


# def simple_encrypt(s):
#     s1 = ''
#     for i, ch in enumerate(s):
#         pos = ascii_lowercase.find(ch)
#         if pos >= 0:
#             s1 += ascii_lowercase[26 - pos - 1]
#         else:
#             s1 += s[i]
#     return s1

# def simple_encrypt(s):
#     return ''.join([ascii_lowercase[26 - ascii_lowercase.find(ch) - 1] if ascii_lowercase.find(ch) >= 0 else s[i] for i, ch in enumerate(s)])

print(simple_encrypt('!@#'))
print(simple_encrypt('abc'))
