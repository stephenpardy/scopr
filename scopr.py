from contextlib import contextmanager
import inspect

@contextmanager
def scope(isolate=False):
    """Starts a new scope

    Uses the contextmanager to start a new scope by saving a copy of the globals()
    dictionary from the calling function. Will overwrite the globals() dictionary of
    the calling function with the old values, and will delete all newly-set variables.
    Note: This follows normal scoping rules and mutable objects that have been updated
    inside this scope will remain updated unless you specify isolate=True

    kwargs:
        isolate: If True, will make a copy of all mutable objects.

    """
    current_frame = inspect.currentframe()
    outer_frame = inspect.getouterframes(current_frame, 1)
    glbs = dict(outer_frame[2][0].f_globals)  # hold on to the old globals

    if isolate:
        # make a copy of all mutable objects
        import copy
        for key, value in glbs.items():
            if getattr(value, '__setitem__', None) is not None:
                glbs[key] = copy.deepcopy(value)

    try:
        yield
    finally:
        new_variables = set(glbs) ^ set(outer_frame[2][0].f_globals)

        # rewrite the global variables
        for key, value in glbs.items():
            outer_frame[2][0].f_globals[key] = value

        #delete any newly-set variables
        for variable in new_variables:
            del outer_frame[2][0].f_globals[variable]
