import math

def isPerfectSquare(x):

    # Find floating point value of
    # square root of x.
    sr = math.sqrt(x)

    # If square root is an integer
    return ((sr - math.floor(sr)) == 0)

print(isPerfectSquare(5))
