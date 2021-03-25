import inspect
import logging
from functools import wraps
import log_decorator

trace_logger = logging.getLogger("DECORAT_LOG")


def log(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        stack = inspect.stack()
        trace_logger.debug(f"Function {fn.__name__} was called from {stack[1].function}")
        # print(f"Function {fn.__name__} was called from {stack[1].function}")
        return fn(*args, **kwargs)

    return inner


@log
def foo():
    pass


@log
def bar():
    foo()


bar()



