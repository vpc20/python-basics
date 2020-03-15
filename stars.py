import random
from string import ascii_letters, digits, punctuation
import time

for i in range(500):
    for j in range(75):
        rand_num = random.choice(list(range(10)))
        if rand_num in [0]:
            print(" ", end=' ')
        else:
            print(random.choice((' ', '*')), end=' ')
            # print random.choice(ascii_letters + digits + punctuation),
    print('')
    time.sleep(0.11)
