from contextlib import contextmanager
import inspect

@contextmanager
def scope():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 1)

    glbs = dict(calframe[2][0].f_globals)  # hold on to the old globals
    yield
    new_variables = set(glbs) ^ set(calframe[2][0].f_globals)

    # rewrite the global variables
    for k, v in glbs.items():
        calframe[2][0].f_globals[k] = v

    #delete any newly-set variables
    for variable in new_variables:
        del calframe[2][0].f_globals[variable]
