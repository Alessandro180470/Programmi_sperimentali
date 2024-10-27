import statistics

import scipy.stats as stats

# Calcola la probabilità cumulativa di Z fino a 0.34
cumulative_prob = stats.norm.cdf(0.34)
cumulative_prob1 = stats.norm.cdf(-0.34)
# Calcola la probabilità che Z sia maggiore di 0.34
prob = 1 - cumulative_prob
prob1 = 1 - cumulative_prob1
print(prob,prob1)

import numpy as np
import pylab
import scipy.stats as stats



measurements = np.random.normal(loc = 20, scale = 5, size=100)
stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()
