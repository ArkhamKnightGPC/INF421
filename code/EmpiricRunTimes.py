import Individual
import BenchmarkFunctions
import EA
import time
import matplotlib.pyplot as plt
from statistics import mean 

def PlotOneMaxRunTime():
    '''
    Generates scatter plot for empirical run time analysis using (1+1) EA and the OneMax benchmark function
    '''
    nvals = [10, 20, 30, 40, 50]
    run_times = []

    for n in nvals:

        number_of_trials = 30
        current_trial = 1
        trial_run_times = []

        while(current_trial <= number_of_trials):

            start_time = time.process_time() #we measure start time before running the EA
            solution = EA.EvolutionaryAlgorithm(BenchmarkFunctions.OneMax, n)
            end_time = time.process_time() #we measure end time after running the EA

            trial_run_times.append(end_time - start_time)
            current_trial += 1

        run_times.append(mean(trial_run_times))

    # Plotting the histogram
    plt.scatter(nvals, run_times, color='blue', marker='o')
    plt.xlabel('Problem Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime for OneMax')
    plt.grid(True)

    #save plot in a png
    plt.savefig('../plots/OneMaxRunTime.png')
    return

def PlotLeadingOnesRunTime():
    '''
    Generates scatter plot for empirical run time analysis using (1+1) EA and the LeadingOnes benchmark function
    '''
    nvals = [10, 20, 30, 40, 50]
    run_times = []

    for n in nvals:

        number_of_trials = 30
        current_trial = 1
        trial_run_times = []

        while(current_trial < number_of_trials):

            start_time = time.process_time() #we measure start time before running the EA
            solution = EA.EvolutionaryAlgorithm(BenchmarkFunctions.LeadingOnes, n)
            end_time = time.process_time() #we measure end time after running the EA

            trial_run_times.append(end_time - start_time)#we use average of measurements as theestimator
            current_trial += 1
        
        run_times.append(mean(trial_run_times))#we use average of measurements as theestimator

    # Plotting the histogram
    plt.scatter(nvals, run_times, color='blue', marker='o')
    plt.xlabel('Problem Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime for LeadingOnes')
    plt.grid(True)

    #save plot in a png
    plt.savefig('../plots/LeadingOnesRunTime.png')
    return
