def hexdump(filename):
    f = open(filename, "rb")
    s1 = f.read()
    s = ''
    i = 0

    for i, b in enumerate(s1):
        if i % 16 == 0:
            print(' ' * 2, s)
            s = ''
        ch = chr(b)
        if ch.isprintable():
            s += ch
        else:
            s += '.'
        print('{:02X}'.format(b), end=' ')

    i += 1
    while i % 16 != 0:
        print('  ', end=' ')
        i += 1
    print(' ' * 2, s)

    f.close()


# hexdump(r"C:\Temp\wf-01.hccapx")
# hexdump(r"C:\Temp\reverse")
# hexdump(r"C:\Temp\sample1.txt")
hexdump(r"sample.txt")

