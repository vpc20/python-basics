a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)  # original array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::-1])  # reversed [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[-1::-1])  # reversed [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[0])  # head 1
print(a[1:])  # tail [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:-1])  # leading [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])  # last 10
print(a[5:])  # 6th element to the last [6, 7, 8, 9, 10]
print(a[4::-1])  # 5th element to the start (reversed) [5, 4, 3, 2, 1]
print(a[-1:-6:-1])  # last element to the 6th (reversed) [10, 9, 8, 7, 6]
print(a[-1:4:-1])  # last element to the 6th (reversed) [10, 9, 8, 7, 6]
print(a[1:-1])  # remove first and last char [2, 3, 4, 5, 6, 7, 8, 9]
print(a[-2:0:-1])  # remove first and last char (reversed) [9, 8, 7, 6, 5, 4, 3, 2]
print(a[1::2])  # every 2nd element [2, 4, 6, 8, 10]
print(a[2::3])  # every 3nd element [3, 6, 9]
print(a[-2::-2])  # every 2nd element (reversed) [9, 7, 5, 3, 1]
print(a[-3::-3])  # every 3rd element (reversed) [8, 5, 2]
