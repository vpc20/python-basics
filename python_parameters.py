def function_with_arbitrary_arguments(*args):
    if len(args) == 0:
        print('No arguments passed to function')
    for arg in args:
        print(arg)


def function_with_arbitrary_keyworded_arguments(**params):
    print(params.get('color'))
    print(params.get('size'))
    print(list(params.keys()))
    print(list(params.items()))

    for param_keys in params.keys():
        print(param_keys)
    print('*' * 50)

    for param_values in params.values():
        print(param_values)
    print('*' * 50)

    for param_items in params.items():
        print(param_items)


function_with_arbitrary_arguments()
print('*' * 50)
function_with_arbitrary_arguments(1, 2, 3, 4, 5)
print('*' * 50)
function_with_arbitrary_arguments('Python', 'Ruby', 'C#')
print('*' * 50)
function_with_arbitrary_keyworded_arguments(color='blue', size='medium')
