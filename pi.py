def _arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x*x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def pi(bits):
    '''Calculate Pi using Machin's formula
    '''
    unity = 2**(bits + 10)
    pi = 4 * (4*_arccot(5, unity) - _arccot(239, unity))
    return pi // 2**10
