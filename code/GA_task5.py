import random
import heapq
import numpy as np
from itertools import combinations
from Individual import Individual
from EA import generateRandomOffspring

def GenerateOnPlateau(n, k):
    """
    Creates individual with k ones. Positions are chosen uniformly at random
    """
    random_permutation = np.random.permutation(range(0, n)) #we pick first n-k numbers in a random permutation of [1..n]
    individual = Individual(n)
    for i in range(n-k):
        bit_idx = random_permutation[i]
        individual.set(bit_idx)
    return individual

def HammingDistance(individual1, individual2):
    n = individual1.size
    dist = 0
    for i in range(n):
        bit1 = individual1.get(i)
        bit2 = individual2.get(i)
        dist += (bit1 + bit2)%2
    return dist

def Diversity(Pt, k):
    diversity = 0
    #we compute hamming distance between all pairs of individuals in the population
    for individual1 in Pt:
        for individual2 in Pt:
            dist = HammingDistance(individual1[1], individual2[1])
            if(dist == 2*k):
                diversity += 1 #add to diversity pairs with maximum distance
    return diversity/2 #we divide by 2 because each pair is counted twice

def GeneticAlgorithm2(f, n, k, mu, lamb, pc, max_iter = 50):
    """
    (mu + lambda) Genetic Algorithm with recombination rate pc for Task5
    """
    t = 0
    Pt = []
    diversities = []
    found_optimum = -1 #used to store time we find optimum
    
    for _ in range(mu):# we must create a random initial population of size mu
        individual = GenerateOnPlateau(n, k)
        fitness = f(individual, k)
        pair_fitness_individual = (fitness, individual) #we create pair (fitness, individual)
        Pt.append(pair_fitness_individual)

    heapq.heapify(Pt) # we transform population into a priority queue

    while True:

        diversity = Diversity(Pt, k) #we compute diversity of population
        diversities.append(diversity)
        total_pairs = (n*(n-1))/2
        if diversity >= total_pairs/4: #if diversity >= a fourth of total pairs, we break
            return diversities, found_optimum
        
        if(t >= max_iter): #if we reach max iterations, we also break
            return diversities, found_optimum
        
        t += 1
        offspring = []

        for _ in range(lamb): #in each iteration, we will generate an individual in the offspring
            branch_decider = random.uniform(0, 1)

            if(branch_decider < pc): #we perform recombination with probability pc
                individual1 = random.choice(Pt)[1]
                individual2 = random.choice(Pt)[1]
                new_individual = Individual(n)
                for i in range(n):
                    #for each bit, we chose uniformly at random between bit value in individual1 and individual2
                    bit_value = random.choice([individual1.get(i), individual2.get(i)])
                    if(bit_value == 1): #if chosen value is 1, we set bit in offspring
                        new_individual.set(i)
                offspring.append(new_individual)
            else: #else we do normal EA iteration
                offspring.append(generateRandomOffspring(random.choice(Pt)[1], 1 / n))

        while(len(offspring) > 0):
            candidate_individual = offspring.pop(0)
            fitness = f(candidate_individual, k)

            if(candidate_individual.count() == n and found_optimum == -1):
                #optimum must come from the offspring at some point
                found_optimum = t

            #we add candidate_individual to the priority queue and pop least fit individual
            heapq.heappushpop(Pt, (fitness, candidate_individual))
