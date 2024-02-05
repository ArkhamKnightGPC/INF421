import time
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import Individual
import GA_task5
import BenchmarkFunctions

def PlotGeneticAlgorithmDiversities():
    """
    Generates scatter plot for empirical run time analysis using (mu + lambda) GA and the Jumpk benchmark function
    """
    #we set parameter values for our tests
    test_values = [(300, 4, 5, 1, 0), #base values
            (300, 5, 5, 1, 0), (300, 6, 5, 1, 0), #testing influence of k
            (300, 4, 10, 1, 0), (300, 4, 15, 1, 0), #testing influence of mu
            (300, 4, 5, 5, 0), (300, 4, 5, 10, 0), #testing influence of lambda
            (300, 4, 5, 1, 0.5), (300, 4, 5, 1, 1)] #testing influence of pc

    plot_number=1

    for n, k, mu, lamb, pc in test_values:

        diversities, found_optimum = GA_task5.GeneticAlgorithm2(BenchmarkFunctions.JumpK, n, k, mu, lamb, pc)

        # we make a scatter plot
        plt.figure()
        plt.scatter(range(1, len(diversities)+1), diversities, color='blue', marker='o', label='Diversity evolution')
        plt.scatter(range(found_optimum, found_optimum+1), diversities[found_optimum], color='red', marker='o', label='Found optimum')    
        plt.xlabel('t')
        plt.ylabel('diversity')
        plt.title(f'Test for n={n} k={k} mu={mu} lambda={lamb} pc={pc}')
        plt.grid(True)
        plt.legend()

        #save plot in a png
        plt.savefig(f'../plots/GAplots6/GAtest{plot_number}.png')
        plot_number+=1
