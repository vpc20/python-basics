import os

print(os.curdir)
print(os.pardir)
print(os.defpath)
print(os.sep)
print(os.altsep)
print(os.pathsep)
print(os.devnull)
print(os.error)

for k, v in os.environ.items():
    print(k, v)

print(os.extsep)
print(os.fsencode)
print(os.fsdecode)