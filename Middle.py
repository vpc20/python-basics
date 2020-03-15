s1 = 'abcd'
s2 = 'abcde'

print(s1)
mid = int(len(s1) / 2)
print(s1[:mid], s1[mid:])
print(s1[mid])

print('=' * 32)

mid = int(len(s2) / 2)
print(s2)
print(s2[:mid], s2[mid:])
print(s2[mid])

print('=' * 32)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mid = int(len(a) / 2)
print(mid)
print(a[:mid])
print(a[mid:])

for i in range(mid):
    print(a[i], a[len(a) - i - 1])
