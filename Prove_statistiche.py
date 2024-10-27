import statistics

import numpy as np

X = [35, 42, 36, 33, 31, 40, 33, 35, 47, 33, 30]
Y = [10, 20, 30, 40, 50]
statistics.geometric_mean(X)  # 35.5994077168891
statistics.harmonic_mean(X)  # 35.31218049963092
statistics.mean(X)  # 35.90909090909091
statistics.median(X)  # 35
statistics.mode(X)  # 33
statistics.pstdev(X)  # 4.888847148999546
statistics.pvariance(X)  # 23.90082644628099
statistics.quantiles(X)  # [33.0, 35.0, 40.0]
statistics.quantiles(X, n=4)  # [33.0, 35.0, 40.0]
statistics.quantiles(X, n=10)  # [30.2, 31.8, 33.0, 33.0, 35.0, 35.2, 37.6, 41.2, 46.0]
print(statistics.pvariance(X),statistics.quantiles(X),statistics.pstdev(X))
print(statistics.pvariance(Y),statistics.quantiles(Y))
# Calculating variance
data = np.array([35, 42, 36, 33, 31, 40, 33, 35, 47, 33, 30])
variance = np.var(data)
# Calculating standard deviation
std_deviation = np.std(data)
percentile_50 = np.percentile(data, 75)
print(percentile_50)
print(variance)
print(std_deviation)

from sklearn.metrics import r2_score
X = [35, 42, 36, 33, 31, 40, 33, 35, 47, 33, 30]
Xp = [32, 42, 35, 33, 31, 41.1, 33, 34.9, 45, 32, 25]
#calcola il coefficiente di detrminazione tra i dati X e quelli stimati
# Assuming y_true contains the observed values and y_pred contains the predicted values
r2 = r2_score(X, Xp)
print("R-squared:", r2)