from tvm import relay
from aot import compile
import sys


def identity():
    """The float32 identity function in Relay.
    """
    x = relay.var('x', shape=())
    f = relay.Function([x], x)
    return f


def simple_example(func):
    if '-r' in sys.argv[1:]:
        # Dump the Relay representation (for educational purposes).
        print(func)
    else:
        # Compile the function and print the FuTIL.
        print(compile(func))


if __name__ == '__main__':
    simple_example(identity())
