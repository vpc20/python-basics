import os

path = os.environ.get('PATH')
pathnames = sorted(path.split(';'))
print(len(pathnames))

print('-------------------------------------')
print('Values for PATH environment variable:')
for pathname in pathnames:
    print(pathname)

dup_count = 0
print('------------------------------------')
print('Duplicate PATH environment variable:')
for i in range(len(pathnames)):
    for j in range(i + 1, len(pathnames)):
        if pathnames[i] == pathnames[j]:
            print(pathnames[i])
            dup_count += 1
            break
if dup_count == 0:
    print('*** No duplicate paths ***')

