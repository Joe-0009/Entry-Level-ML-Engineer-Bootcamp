import numpy as np
import sys


def rev_swap():
    print(" ".join(sys.argv[1:])[::-1].swapcase())


rev_swap()
