n = 123456789
print('{:,}'.format(n))
print(f'{n:,}')

f = 1234.123456789
print('{:,.2f}'.format(f))
print(f'{f:,.2f}')

print('{:10,.2f}'.format(f))
print(f'{f:10,.2f}')

print('{:010,.2f}'.format(f))
print(f'{f:010,.2f}')
print('')

print('\x1b[4;30;47mBSSID               \x1b[0m', end='  ')
print('\x1b[4;30;47mMac Addr            \x1b[0m', end='  ')
print('\x1b[4;30;47mSignal  \x1b[0m', end='  ')
print('\x1b[4;30;47mVendor              \x1b[0m')
print('{:20.20}  {:20.20}  {:>8.8}  {:20.20}'.format('AndroidAPJ7', 'DE:AD:BE:EF ', '-88dBm', 'Samsung'))
print(
    '{:20.20}  {:20.20}  {:>8.8}  {:20.20}'.format('Iphonexxxxzzzzxccvdfgrtgftygt', 'C0:FE:FE:ED ', '-30dBm', 'Apple'))

print(f'{"AndroidAPJ7":20.20}  {"DE:AD:BE:EF ":20.20}  {"-88dBm":>8.8}  {"Samsung":20.20}')
