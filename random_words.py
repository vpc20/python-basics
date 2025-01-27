import random
from string import ascii_uppercase, ascii_lowercase


def random_word():
    word = ''
    word_length = 0
    prev_ch = ''
    while word_length == 0:
        word_length = random.randrange(11)
    for i in range(word_length):
        if prev_ch in 'aeiou':
            ch = random.choice(ascii_lowercase)
        else:
            ch = random.choice('aeiou')
        word = word + ch
        prev_ch = ch
    return word


def random_words(n):
    words = ''
    for i in range(1, n + 1):
        words = words + ' ' + random_word()
    return words.strip()


# print random_word()
# print random_words(1)
# print random_words(2)
# print random_words(3)
# print random_words(4)
print(random_words(100))


class ClassName:
    def __init__(self, param):
        self.param = param
