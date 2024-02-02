from Individual import Individual
import numpy as np

def generateRandomOffspring(x, p):
    """
    Generate a copy of x flipping each bit independently with probability p
    """
    n = x.size
    y = Individual(n)
    for idx in range(n):
        xi = x.get(idx)
        rand_var = np.random.uniform(0, 1)
        #bit idx in y is 1 if and only if
        mutated_to_one = (rand_var < p and xi == 0) #mutated from 0 to 1 (with probability p)
        stayed_one = (rand_var >= p and xi == 1) #did not mutate, was already 1 (probability 1-p)
        if (mutated_to_one or stayed_one): 
            y.set(idx)
    return y

def EvolutionaryAlgorithm(f, n):
    """
    (1+1) Evolutionary Algorithm
    """
    t = 0
    Pt = generateRandomOffspring(Individual(n), 0.5)  # random initial solution

    while f(Pt) < n:
        y = generateRandomOffspring(Pt, 1 / n)
        if f(y) > f(Pt):  # we pick solution that maximizes f
            Pt = y
        t += 1

    return Pt
