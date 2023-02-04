# Importing module
import importlib

if __name__ == '__main__':

    # Importing the created module using the
    # import_module function into a variable
    mod = importlib.import_module('Hayan/Algorithms/AES')

    # Printing the name of module
    print(mod.__name__)

    # Calling the function from the imported module
    mod.construct()

    # Importing the created module using the
    # import_module function into a variable
    mod = importlib.import_module('mod2')

    # Printing the name of module
    print(mod.__name__)

    # Calling the function from the imported
    # module
    mod.main()
