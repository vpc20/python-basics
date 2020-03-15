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


print_format_table()
