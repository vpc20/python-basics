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
            print('***unicode error', line)
            break
        else:
            print(line, end='')
            # print(len(line))


# read_text_file1('UnitTest.py')

# read_text_file1(r'c:\users\vpc\share\rockyou.txt')

read_text_file1('timer.py')
print(f'\n{("=" * 96)}\n')
read_text_file2('UnitTest.py')

s1 = f"""
   line1
      line2
         line3
   line1a      
"""

outf = open('outfile.txt', 'w')
outf.close()

outf = open('outfile.txt', 'a')
outf.write(s1)
outf.close()


