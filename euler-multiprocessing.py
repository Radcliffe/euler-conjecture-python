import sys
from math import gcd
from itertools import combinations_with_replacement
from multiprocessing import Pool

class Search:
    def __init__(self, pool_size, powers, sums_of_powers):
        self.pool_size = pool_size
        self.powers = powers
        self.sums_of_powers = sums_of_powers
    
    def __call__(self, start):
        for e, e_5 in self.powers[start::self.pool_size]:
            half = e_5 // 2
            for val, (a, b) in self.sums_of_powers.items():
                if val > half:
                    break
                if e_5 - val in self.sums_of_powers:
                    c, d = self.sums_of_powers[e_5 - val]
                    if b < c and gcd(a, b, c, d) == 1:
                        print(a, b, c, d, e)

if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
    except:
        N = 150
    try:
        pool_size = int(sys.argv[2])
    except:
        pool_size = 4

    powers = [(a, a**5) for a in range(1, N)]
    sums_of_powers =  dict(
        sorted([(a5 + b5, (a, b))
                for (a, a5), (b, b5) in combinations_with_replacement(powers, 2)
                ]))
    with Pool(pool_size) as pool:
        search = Search(pool_size, powers, sums_of_powers)
        pool.map(search, range(pool_size))

