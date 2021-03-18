import os


def print_dir(currpath):
    def prtdir(path, lvl):
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                if dirname != dirnames[-1]:
                    if lvl == 0:
                        print(f'├{"    " * lvl}── {dirname}')
                    else:
                        print(f'{"│    " * lvl}├── {dirname}')
                else:
                    if lvl == 0:
                        print(f'└{"    " * lvl}── {dirname}')
                    else:
                        print(f'{"│    " * lvl}└── {dirname}')
                # if dirname != dirnames[-1]:
                #     if lvl == 0:
                #         print(f'├{"   " * lvl}── {dirname}')
                #     else:
                #         print(f'│{"   " * lvl}└── {dirname}')
                # else:
                #     if lvl == 0:
                #         print(f'└── {dirname}')
                #     else:
                #         print(f'│{"   " * lvl}└── {dirname}')
                prtdir(os.path.join(dirpath, dirname), lvl + 1)
            dirnames.clear()  # we're doing recursion so we only need to process one level directory for os.walk
            # for filename in filenames:
            #     if filename != filenames[-1]:
            #         print(f'   ├{"────" * lvl} {filename}')
            #     else:
            #         print(f'   ├{"────" * lvl} {filename}')
                    # print(f'{"   " * lvl}└─── {filename}')
                # print(os.path.join(dirpath, filename))

    print(currpath)
    prtdir(currpath, 0)


# print_dir('c:\\go')
print_dir(r'c:\\temp')
# print_dir(r'C:\Users\vpc\PycharmProjects\PythonBasics')

