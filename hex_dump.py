def hexdump(filename):
    f = open(filename, "rb")
    s1 = f.read()
    s = ''

    for i, b in enumerate(s1):
        if i % 16 == 0:
            print(' ' * 2, s)
            s = ''
        ch = chr(b)
        s += ch if ch.isprintable() else '.'
        print(f'{b:02X}', end=' ')

    remaining = 16 - len(s)  # to fill up hex portion with with spaces before printing the string s
    print(' ' * (remaining * 3), end='   ')
    print(s)

    f.close()


# hexdump(r"C:\Temp\wf-01.hccapx")
# hexdump(r"C:\Temp\reverse")
# hexdump(r"C:\Temp\sample1.txt")
# hexdump(r"sample.txt")
# hexdump(r'C:\appverifUI.dll')
hexdump(r'C:\vfcompat.dll')
