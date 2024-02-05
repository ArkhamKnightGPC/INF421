import numpy as np
from math import comb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def calculate_coefficients(n, p):
    P = [[[0.0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    # Base case: m
    for m in range(1, n + 1):
        for j in range(m + 1):
            denominator = sum(comb(m, k) * (p ** k) * ((1 - p) ** (m - k)) for k in range(m + 1))
            P[m][0][j] = comb(m, j) * (p ** j) * ((1 - p) ** (m - j)) / denominator

    # Recurrence relation
    for m in range(2, n + 1):
        for i in range(1, m + 1):
            for j in range(i, m + 1):
                P[m][i][j] = p * P[m - 1][i - 1][j] + (1 - p) * P[m - 1][i - 1][j - 1]

    # Calculate p_i
    p_i = [0.0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n + 1):
            p_i[i] += P[n][i][j]

    return p_i

# Set up values for n
n_values = list(range(2, 101))  # Change the range as needed

# Calculate the sum for each n
sum_values = []
for n in n_values:
    coefficients = calculate_coefficients(n, 1 / n)
    sum_val = sum(1 / p if p != 0 else 0 for p in coefficients)  # Include i = 0
    sum_values.append(sum_val)

# Plot the sum as a function of n
plt.figure()
plt.plot(n_values, sum_values)
plt.xlabel('n')
plt.ylabel('Sum')
plt.title('Sum of 1 / p_i vs. n')
plt.grid(True)
plt.savefig('../plots/OneMaxTheoreticalRunTime.png')

#function for fitting
def fit_function(y, a):
    return a * y * np.log(y)

# Perform curve fitting
popt, pcov = curve_fit(fit_function, n_values, sum_values, maxfev=10000) # maxfev increased for more iterations

# Plot the data and fitted curve
plt.figure()
plt.scatter(n_values, sum_values, label='Run time estimate')
plt.plot(n_values, fit_function(np.array(n_values), *popt), 'r-', label='O(n log n) fitted curve')
plt.xlabel('n')
plt.ylabel('Run time')
plt.legend()
plt.grid(True)
plt.savefig('../plots/OneMaxTheoreticalRunTimeFit.png')
