from miller_rabin import is_probable_prime
from div import division_test

import sys
import multiprocessing
import time

def bit_size(x):
    size = 0
    while x > 0:
        x = x >> 1
        size = size + 1
    return size

step = 2**64
blocksize = 10000

def search_safe_prime(start):
    x = start
    for c in range(blocksize):
        xs = (x - 1) >> 1

        if (division_test(xs, x)
            and is_probable_prime(xs) and is_probable_prime(x)):
            return x

        x = x + step

    return None

def found_prime(p, start):
    print ('')
    print ('Fount safe prime: {0} bits'.format(bit_size(p)))
    print (hex(p))
    print ('Difference from start:')
    print ((p - start) / step)

def check_group(start):
    s = start
    while True:
        p = search_safe_prime(s)
        if p:
            found_prime(p, start)
            return
        s = s + blocksize * step

        sys.stdout.write('+')
        sys.stdout.flush()

queue = multiprocessing.Queue()

def search_safe_prime_process(start):
    p = search_safe_prime(start)
    if p:
        queue.put(p)

def check_group_multiprocess(start):
    s = start
    while queue.qsize() == 0:
        if len(multiprocessing.active_children()) >= multiprocessing.cpu_count():
            time.sleep(0.1)
        else:
            p = multiprocessing.Process(target=search_safe_prime_process, args=(s,))
            p.start()
            s = s + blocksize * step

            sys.stdout.write('+')
            sys.stdout.flush()

    results = []

    while queue.qsize() > 0 or len(multiprocessing.active_children()) > 0:
        if queue.qsize() > 0:
            results.append(queue.get())
        else:
            time.sleep(5)

    found_prime(min(results), start)
