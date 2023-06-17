import random

i = 0
while i < 6:
    print(random.randrange(1, 43), end=' ')
    i += 1
print('')

for i in range(6):
    print(random.randrange(1, 43), end=' ')
print('')

picked = []
num_ctr = 0
while num_ctr < 6:
    x = random.randint(1, 42)
    if x not in picked:
        print(x, end=" ")
        picked.append(x)
        num_ctr += 1
print("")