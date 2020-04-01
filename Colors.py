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

FG_WHITE = 30
FG_RED = 31
FG_GREEN = 32
FG_BROWN = 33
FG_BLUE = 34
FG_MAGENTA = 35
FG_CYAN = 36
FG_GRAY = 37
FG_BLACK = 38

BG_WHITE = 40
BG_RED = 41
BG_GREEN = 42
BG_BROWN = 43
BG_BLUE = 44
BG_MAGENTA = 45
BG_CYAN = 46
BG_GRAY = 47
BG_BLACK = 48

NORMAL = 0
BOLD = 1
ITALIC = 3
UNDERLINE = 4
REVERSE = 7


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
print_color("hello", NORMAL, FG_RED, BG_GRAY)
print_color("hello", BOLD, FG_RED, BG_GRAY)
print_color("hello", ITALIC, FG_RED, BG_GRAY)
print_color("hello", UNDERLINE, FG_RED, BG_GRAY)
print_color("hello", NORMAL, FG_WHITE, BG_CYAN)
print_color("hello", REVERSE, FG_RED, BG_BLACK)















