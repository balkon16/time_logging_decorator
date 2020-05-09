from functools import wraps
import time
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

def logged(function):
    @wraps(function)
    def with_time_logging(*args, **kwargs):
        logging.debug('Function {} called'.format(function.__name__))
        t0 = time.time()
        res = function(*args, **kwargs)
        t1 = time.time()
        logging.info('Function {} took {} seconds'.format(function.__name__, t1 - t0))
        return res
    return with_time_logging

@logged
def time_consuming_func(x):
    """Docstring for the time_consuming_func."""

    time.sleep(5)
    return x * 2

time_consuming_func(25)
