###############################################################################################################################
# coding=utf-8
#
# pi_gcd.py
#
#  Copyright (c) 2020  Mark Sattolo  <epistemik@gmail.com>

__author__         = 'Mark Sattolo'
__author_email__   = 'epistemik@gmail.com'
__python_version__ = '3.6+'
__created__ = '2020-04-10'
__updated__ = '2020-04-10'

# Inspiration:
#     Matt Parker: Generating π from 1,000 random numbers
#     https://www.youtube.com/watch?v=RZBhSi_PwHU


def pi_estimate(num_samples:int, num_range:int, num_runs:int=10):

    import math
    import random

    print(F"            pi = {math.pi:>11.11f}")

    for r in range(num_runs):
        coprime = 0
        for i in range(num_samples):
            a = random.randrange(1,num_range)
            b = random.randrange(1,num_range)

            if math.gcd(a,b) == 1:
                coprime += 1

        fraction_coprime = coprime/num_samples

        est = math.sqrt(6.0/fraction_coprime)

        print(F"estimate of pi = {est:>11.11f}")


if __name__ == '__main__':
    pi_estimate(1000000,1000000)
    exit()
