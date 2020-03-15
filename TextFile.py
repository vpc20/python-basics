def read_text_file1(filename):
    inf = open(filename)
    for line in inf:
        print(line, end='')
    inf.close()


def read_text_file2(filename):
    inf = open(filename)
    line = 'dummy'
    while line:
        try:
            line = inf.readline()
        except UnicodeDecodeError:
            print('unicode error', line)
        else:
            print(line, end='')
            # print(len(line))


read_text_file1('UnitTest.py')
print(f'\n{("=" * 96)}\n')
read_text_file2('UnitTest.py')
