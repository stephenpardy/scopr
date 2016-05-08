# scopr
Ham-fisted scoping in Python

Load it into your project and enjoy scopes anywhere:

    from scopr import scope

    a = 1  # define a variable outside the scope
    with scope():
        a = 2  # redefine and use a variable here

    print(a)  # prints 1


Works on CPython with Python 2 and 3, and on PyPy.
CAUTION: This is mostly untested and definitely a bad idea.
