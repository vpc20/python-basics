import sys

arg_list = sys.argv
print("Complete list of system arguments:", arg_list)
print("Program:", arg_list[0])

print("List of program arguments:")
for i in range(1, len(arg_list)):
    print(" ", i, arg_list[i])
