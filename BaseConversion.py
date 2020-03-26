print(bin(15))
print(hex(15))
print(int('1111', 2))
print(int('f', 16))

print('-----------------')
print(hex(int('1111', 2)))  # binary to hex
print(bin(int('ff', 16)))  # hex to binary
print(int('v', 32))  # base must be >= 2 and <= 36

