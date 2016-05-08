from contextlib import contextmanager
import inspect

@contextmanager
def scope():
    current_frame = inspect.currentframe()
    outer_frame = inspect.getouterframes(current_frame, 1)

    glbs = dict(outer_frame[2][0].f_globals)  # hold on to the old globals
    yield
    new_variables = set(glbs) ^ set(outer_frame[2][0].f_globals)

    # rewrite the global variables
    for key, value in glbs.items():
        outer_frame[2][0].f_globals[key] = value

    #delete any newly-set variables
    for variable in new_variables:
        del outer_frame[2][0].f_globals[variable]
