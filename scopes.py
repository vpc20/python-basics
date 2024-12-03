def enclosing_function():
    var = "value"

    def nested_function():
        # Using the nonlocal statement, the variable is now modifiable from the local scope
        nonlocal var
        var = "new_value"

    nested_function()
    print(var)


enclosing_function()

###############################################################
global_var = 10


def some_function():
    # Similar to the nonlocal statement, Python provides the global statement to allow the modification of global names
    # from a local scope.
    global global_var
    global_var = 20


some_function()

print(global_var)
