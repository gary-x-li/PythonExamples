#!/usr/bin/env python3
from collections import OrderedDict
from pprint import pprint
import random
import numpy as np
from timeit import default_timer as timer
import os
from pathlib import Path
import sys


def hello():
    od = OrderedDict([('b', 2), ('a', 1)])
    print(od.keys())

    d = {'b': 2, 'a': 1}
    print(d.keys())

    print([3] * 4)
    print([i for i in range(10)])
    print(list(range(1, 11)))

    print(sys.path)
    print(__file__)
    print(Path.cwd().joinpath('./resources/test.csv'))
    p = Path.cwd().joinpath('./resources/test.csv')
    print(p.is_file())

    # start = timer()
    # for _ in range(1000):
    #     #random.choices(list(range(30_000)))
    #     np.random.choice(list(range(30_000)), size=(1,))
    # end = timer()
    # print(end - start)


if __name__ == '__main__':
    hello()
