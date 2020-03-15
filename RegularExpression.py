import re

# single character
print(re.findall(r'a.*b', 'abcdefgac'))
print(re.search(r'[0-9]', '0').string)  # scan through string looking for a match to the pattern
print(re.match(r'[0-9]', '0').string)  # apply the pattern at the start of the string

print(bool(re.search(r'[0-9]', 'a10')))
print(bool(re.match(r'[0-9]', '10')))

print('--------------')
print(bool(re.fullmatch(r'[0-9]', '1')))
print(bool(re.fullmatch(r'\d\d\d', '123')))
print(bool(re.fullmatch(r'\d\d\d', '123')))

print(re.findall(r'[0-9]', '01234567890'))
print(re.findall(r'[a-z]', 'abcdefghij'))

# two characters
print(re.findall(r'[a-z][0-9]', 'a1d4i9'))

# + means one or more
print(re.findall(r'a+', 'a aa aaa'))
print(re.findall(r'[a-z]+', 'a aa aaa ab abc x'))
print(re.findall(r'[0-9]+', '13 1 1776'))
print(re.findall(r'[0-9]+%', '5%20%99%'))
print(re.findall(r'[a-z]+[0-9]+', 'abc123 a1 a123 bbb1'))

# | means OR/Disjunction
print(re.findall(r'[a-z]+|[0-9]+', 'abc 123 a 1 bbbx 1'))  # letters or digits

# ? means optional
print(re.findall(r'-?[0-9]+', '-123 456 2'))  # negative sign is optional

# identifirers   * means zero or more
print(re.findall(r'[A-Za-z][A-Za-z0-9_]*', 'a B s1 ch1 xx21 int var while CONST'))

# number with negative sign/decimal point
print(re.findall(r'-?[0-9]+\.?[0-9]*', '1 1. 1.0 25 45. 14.25 -1 -2. -34.56'))

# matchgrp = re.match(r'-?[0-9]+', '-123 456 2')
# print matchgrp.group()

print(re.findall(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', '255.255.255.255'))
print(re.findall(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', '255.255.255.255'))

print(re.search(r'^(\d{1,3}\.){3}\d{1,3}$', '255.255.255.255'))

print(re.search(r'^[A-Za-z0-9]{6,}$', 'Aa1234567'))

print(re.search(r'^\d{1,2}[-/]\d{1,2}[-/]\d{4}$', '02/05/2005'))

print(re.search(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', '02-05-2005 00:00'))

print(re.search(r'^\d{4}[- ]?\d{3}[- ]?\d{4}$', '1234-123-1234'))
print(re.search(r'^\d{4}[- ]?\d{3}[- ]?\d{4}$', '12341231234'))
print(re.search(r'^\d{4}[- ]?\d{3}[- ]?\d{4}$', '1234 123 1234'))

























