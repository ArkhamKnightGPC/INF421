from Individual import Individual
import numpy as np
import random
import heapq

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

    while Pt.count() < n:
        y = generateRandomOffspring(Pt, 1 / n)
        if f(y) > f(Pt):  # we pick solution that maximizes f
            Pt = y
        t += 1

    return Pt

def EvolutionaryAlgorithm2(f, n, mu):
    """
    (mu + 1) Evolutionary Algorithm
    """
    t = 0
    Pt = []
    
    for _ in range(mu):# we must create a random initial population of size mu
        individual = generateRandomOffspring(Individual(n), 0.5)
        pair_fitness_individual = (f(individual), individual) #we create pair (fitness, individual)
        Pt.append(pair_fitness_individual)

    heapq.heapify(Pt) # we transform population into a priority queue

    while True:

        most_fit_individual = max(Pt)
        if(most_fit_individual[1].count() == n):
            return most_fit_individual[1]
            
        offspring = generateRandomOffspring(random.choice(Pt)[1], 1 / n)

        heapq.heappushpop(Pt, (f(offspring), offspring)) #we add offspring to the priority queue and pop least fit individual
        t += 1