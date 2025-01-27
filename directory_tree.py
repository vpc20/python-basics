import os


def print_dir(currpath):
    def prtdir(path, lvl, lastdirs):
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                pref = ''
                for lastdir in lastdirs:
                    if lastdir:
                        pref += '    '
                    else:
                        pref += '│   '
                if dirname != dirnames[-1]:
                    print(f'{pref}├── {dirname}')
                else:
                    print(f'{pref}└── {dirname}')
                prtdir(os.path.join(dirpath, dirname), lvl + 1, lastdirs + [dirname == dirnames[-1]])
            dirnames.clear()  # we're doing recursion so we only need to process one level directory for os.walk

    print(currpath)
    prtdir(currpath, 0, [])


# print_dir('c:\\go')
print_dir(r'c:\\temp')
# print_dir(r'C:\Users\vpc\PycharmProjects\PythonBasics')
