import time

from homework3.task2 import multiprocessing_sum_calculation


def test_sum_of_500_with_50_processes():
    """Testing that multiprocessing slow calculation takes less than
     a minute"""
    time_start = time.time()
    multiprocessing_sum_calculation(numbers=range(500), processes=50)
    timing = time.time() - time_start
    assert timing < 60
