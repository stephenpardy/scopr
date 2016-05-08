from contextlib import contextmanager
import inspect

@contextmanager
def scope():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 1)
    glbs = dict(calframe[2][0].f_globals)
    yield
    new_variables = set(glbs) ^ set(calframe[2][0].f_globals)
    for k, v in glbs.items():
        calframe[2][0].f_globals[k] = v

    for variable in new_variables:
        del calframe[2][0].f_globals[variable]
