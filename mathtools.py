def isPrime(n):
    '''Returns true if a number n is a prime number'''
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

def geometric(a, ratio, n):
    '''Calculates the sum of a geometric serie of n elements.
       A geometric sequence is of the form: a, a*r, a*r*r, a*r*r*r,...
       n is the number of elements in the sequence.'''
    #Get the geometric sequence
    sequence = [a*(ratio**x) for x in range(n)]
    #Calculates its sum
    return sum(sequence)