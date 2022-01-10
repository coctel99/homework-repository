"""
Here's a not very efficient calculation function that calculates
something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):
    ""Some weird voodoo magic calculations""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))
Calculate total sum of slow_calculate() of all numbers starting
from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Iterable


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocessing_sum_calculation(numbers: Iterable[int],
                                    processes: int = 1) -> int:
    """
    Calculates sum of elements of iterable with specified number of processes
    :param numbers: Iterable with integer numbers
    :param processes: Number of processes
    :return: Sum of elements got by slow_calculate function
    """
    pool = Pool(processes=processes)
    return sum(pool.map(slow_calculate, numbers))
