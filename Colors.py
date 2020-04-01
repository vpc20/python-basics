# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
#     for style in range(8):
#         for fg in range(30, 38):
#             s1 = ''
#             for bg in range(40, 49):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#             print(s1)
#         print('\n')

WHITE = 30
RED = 31
GREEN = 32
BROWN = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
GRAY = 37
BLACK = 37

NORMAL = 0
BOLD = 1
ITALIC = 3
UNDERLINE = 4


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            for bg in range(40, 49):
                txt_color = ';'.join([str(style), str(fg), str(bg)])
                # print('\x1b[{}m {} \x1b[0m'.format(txt_color, txt_color), end=' ')
                print(f'\x1b[{txt_color}m {txt_color} \x1b[0m', end=' ')
            print('')
        print('')


def print_color(s, style, fg, bg):
    txt_color = ';'.join([str(style), str(fg), str(bg)])
    print(f'\x1b[{txt_color}m{s}\x1b[0m')


print_format_table()
print_color("hello", NORMAL, RED, BLUE)
print_color("hello", BOLD, RED, BLUE)
print_color("hello", ITALIC, RED, BLUE)
print_color("hello", UNDERLINE, RED, BLUE)
