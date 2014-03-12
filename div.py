import math

def gen_primes(max_num):
    'Sieve of Eratosthenes '
    A = range(max_num)
    A[0] = False
    A[1] = False

    for i in range(int(math.sqrt(len(A)))):
        if A[i]:
            for j in range(i*i, len(A), i):
                A[j] = False

    primes = [p for p in A if p]
    return primes

# Primes between 2 and 10000
_prime_nums = gen_primes(10000)
_prime_nums.remove(2)

def division_test(a, b):
    ''' Trial division '''
    assert (a > 10000)
    assert (b > 10000)

    if a & 1 == 0:
        return False
    if b & 1 == 0:
        return False

    for t in _prime_nums:
        if a % t == 0:
            return False
        if b % t == 0:
            return False

    return True
