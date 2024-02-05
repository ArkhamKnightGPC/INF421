import random
import heapq
from Individual import Individual
from EA import generateRandomOffspring

def GeneticAlgorithm(f, n, k, mu, lamb, pc):
    """
    (mu + lambda) Genetic Algorithm with recombination rate pc for Task4
    """
    t = 0
    Pt = []
    most_fit_individual = (0, Individual(n)) #used to store solution
    
    for _ in range(mu):# we must create a random initial population of size mu
        individual = generateRandomOffspring(Individual(n), 0.5)
        fitness = f(individual, k)
        pair_fitness_individual = (fitness, individual) #we create pair (fitness, individual)
        if(fitness > most_fit_individual[0]):
            most_fit_individual = pair_fitness_individual
        Pt.append(pair_fitness_individual)

    heapq.heapify(Pt) # we transform population into a priority queue

    while True:

        if(most_fit_individual[1].count() == n):
            return most_fit_individual
        
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
            else: #else we do normal EA iteration
                offspring.append(generateRandomOffspring(random.choice(Pt)[1], 1 / n))

        while(len(offspring) > 0):
            candidate_individual = offspring.pop(0)
            fitness = f(candidate_individual, k)
            candidate_pair = (fitness, candidate_individual)
            
            if(fitness > most_fit_individual[0]):
                #we update most fit individual if necessary
                most_fit_individual = candidate_pair

            #we add candidate_individual to the priority queue and pop least fit individual
            heapq.heappushpop(Pt, candidate_pair)

        t += 1
