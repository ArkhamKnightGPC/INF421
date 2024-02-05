import time
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import GA_task5
import BenchmarkFunctions

def PlotGeneticAlgorithmDiversities():
    """
    Generates scatter plot for empirical run time analysis using (mu + lambda) GA and the Jumpk benchmark function
    """
    #we set parameter values for our tests
    test_values = [(300, 2, 10, 5, 0.5), #base values n=300, k=4, mu=10, lambda=5, pc=0.5
            (300, 3, 10, 5, 0.5), (300, 4, 10, 5, 0.5), #testing influence of k
            (300, 2, 20, 5, 0.5), (300, 2, 30, 5, 0.5), #testing influence of mu
            (300, 2, 10, 7, 0.5), (300, 2, 10, 10, 0.5), #testing influence of lambda
            (300, 2, 10, 5, 0), (300, 2, 10, 5, 1)] #testing influence of pc

    plot_number=1

    for n, k, mu, lamb, pc in test_values:

        diversities, found_optimum = GA_task5.GeneticAlgorithm2(BenchmarkFunctions.JumpK, n, k, mu, lamb, pc)

        # we make a scatter plot
        plt.figure()
        plt.scatter(range(len(diversities)), diversities, color='blue', marker='o', label='Diversity evolution')
        if(found_optimum > -1):
            plt.scatter(found_optimum, diversities[found_optimum], color='red', marker='o', label=f'Optimum found at t={found_optimum}')
        else:
            plt.scatter([], [], color='red', marker='o', label=f'Optimum never found')
        plt.xlabel('t')
        plt.ylabel('diversity')
        plt.title(f'Test for n={n} k={k} mu={mu} lambda={lamb} pc={pc}')
        plt.grid(True)
        plt.legend()

        #save plot in a png
        plt.savefig(f'../plots/GAplots3/GAtest{plot_number}.png')
        plot_number+=1

PlotGeneticAlgorithmDiversities()
