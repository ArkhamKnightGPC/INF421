import BenchmarkFunctions
import EA
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from statistics import mean 

def PlotOneMaxRunTime():
    """
    Generates scatter plot for empirical run time analysis using (1+1) EA and the OneMax benchmark function
    """
    nvals = range(1, 30)
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

    #function for fitting
    def fit_function(y, a):
        return a * y * np.log(y) #Theoretical analysis points to n log(n) complexity

    # Perform curve fitting
    popt, pcov = curve_fit(fit_function, nvals, run_times, maxfev=10000) # maxfev increased for more iterations

    # we make a scatter plot for run times
    plt.scatter(nvals, run_times, color='blue', marker='o', label='Empirical run time')
    plt.plot(nvals, fit_function(np.array(nvals), *popt), 'r-', label='O(n log n) fitted curve')
    plt.xlabel('Problem Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime for OneMax')
    plt.legend()
    plt.grid(True)

    #save plot in a png
    plt.savefig('../plots/OneMaxRunTime.png')
    return

def PlotLeadingOnesRunTime():
    """
    Generates scatter plot for empirical run time analysis using (1+1) EA and the LeadingOnes benchmark function
    """
    nvals = range(1, 30)
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

    #function for fitting
    def fit_function(y, a):
        return a * y * y #Theoretical analysis points to n^2 complexity

    # Perform curve fitting
    popt, pcov = curve_fit(fit_function, nvals, run_times, maxfev=10000) # maxfev increased for more iterations

    # we make a scatter plot for run times
    plt.scatter(nvals, run_times, color='blue', marker='o', label='Empirical run time')
    plt.plot(nvals, fit_function(np.array(nvals), *popt), 'r-', label='O(n^2) fitted curve')
    plt.xlabel('Problem Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime for LeadingOnes')
    plt.legend()
    plt.grid(True)

    #save plot in a png
    plt.savefig('../plots/LeadingOnesRunTime.png')
    return

def PlotMuPlusOneEAOneMax():
    """
    Generates scatter plot for empirical run time analysis using (mu + 1) EA and the OneMax benchmark function
    """
    n = 30 #we keep n constant and vary only mu
    mu_vals = range(1, 30)
    run_times = []

    for mu in mu_vals:

        number_of_trials = 30
        current_trial = 1
        trial_run_times = []

        while(current_trial < number_of_trials):

            start_time = time.process_time() #we measure start time before running the EA
            solution = EA.EvolutionaryAlgorithm2(BenchmarkFunctions.OneMax, n, mu)
            end_time = time.process_time() #we measure end time after running the EA

            trial_run_times.append(end_time - start_time)#we use average of measurements as theestimator
            current_trial += 1
        
        run_times.append(mean(trial_run_times))#we use average of measurements as theestimator

    #function for fitting
    def fit_function(y, a):
        return a * np.sqrt(y) #Theoretical analysis points to n log(n) complexity

    # Perform curve fitting
    popt, pcov = curve_fit(fit_function, mu_vals, run_times, maxfev=10000) # maxfev increased for more iterations

    # we make a scatter plot
    plt.scatter(mu_vals, run_times, color='blue', marker='o', label='Empirical run time')
    plt.plot(mu_vals, fit_function(np.array(mu_vals), *popt), 'r-', label='O(sqrt n) fitted curve')
    plt.xlabel('mu')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime for OneMax')
    plt.grid(True)
    plt.legend()

    #save plot in a png
    plt.savefig('../plots/OneMaxRunTime2.png')
    return
