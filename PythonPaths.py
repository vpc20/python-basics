import os

print('os.path.realpath = ', os.path.realpath)
print('os.path.pardir   = ', os.path.pardir)
print('os.path.curdir   = ', os.path.curdir)
print('os.path.defpath  = ', os.path.defpath)

print('os.path.devnull  = ', os.path.devnull)

print('os.path.sep      = ', os.path.sep)
print('os.path.altsep   = ', os.path.altsep)
print('os.path.extsep   = ', os.path.extsep)
print('os.path.pathsep  = ', os.path.pathsep)

print(os.path.abspath(os.path.curdir))
print(os.path.abspath(os.path.pardir))

print(os.path.basename(os.path.curdir))
print(os.path.basename(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.basename(os.path.pardir))
print(os.path.basename(r'C:\Users\vpc\PycharmProjects'))

print(os.path.dirname(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.dirname(r'C:\Users\vpc\PycharmProjects'))

print(os.path.exists(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.exists(r'C:\Users\vpc\PycharmProjects\PythonToolsxxx'))

print(os.path.expanduser(r'~\Downloads'))

print(os.path.getatime('pathx.py'))
print(os.path.getctime('pathx.py'))
print(os.path.getmtime('pathx.py'))
print(os.path.getsize('pathx.py'))

print(os.path.isabs(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.isdir(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.isfile(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.islink(r'C:\Users\vpc\PycharmProjects\PythonTools'))

print(os.path.ismount(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.ismount(r'C:\\'))

print(os.path.normcase('C:/Users/vpc/PycharmProjects/PythonTools'))
print(os.path.normpath('C:/Users/vpc/PycharmProjects/PythonTools'))
print(os.path.normpath('C:\\Users\\vpc\\PycharmProjects\\PythonTools'))

print(os.path.split(r'C:\Users\vpc\PycharmProjects\PythonTools'))
print(os.path.split('C:/Users/vpc/PycharmProjects/PythonTools'))
print(os.path.split(r'C:/'))

print(os.path.join('C:/Users/vpc/PycharmProjects', 'PythonTools'))

print(os.path.relpath('C:/Users/vpc/PycharmProjects/PythonTools/.idea/misc.xml'))

print(os.path.splitdrive('C:/Users/vpc/PycharmProjects/PythonTools'))
print(os.path.splitext('C:/Users/vpc/PycharmProjects/PythonTools/cs.py'))







