import statistics


import numpy as np
from matplotlib import pyplot as plt
from numpy import sort

# X = [35, 42, 36, 33, 31, 40, 33, 35, 47, 33, 30]
# Y = [10, 20, 30, 40, 50]
# statistics.geometric_mean(X)  # 35.5994077168891
# statistics.harmonic_mean(X)  # 35.31218049963092
# statistics.mean(X)  # 35.90909090909091
# statistics.median(X)  # 35
# statistics.mode(X)  # 33
# statistics.pstdev(X)  # 4.888847148999546
# statistics.pvariance(X)  # 23.90082644628099
# statistics.quantiles(X)  # [33.0, 35.0, 40.0]
# statistics.quantiles(X, n=4)  # [33.0, 35.0, 40.0]
# statistics.quantiles(X, n=10)  # [30.2, 31.8, 33.0, 33.0, 35.0, 35.2, 37.6, 41.2, 46.0]
# print(statistics.pvariance(X),statistics.quantiles(X),statistics.pstdev(X))
# print(statistics.pvariance(Y),statistics.quantiles(Y))
# # Calculating variance
# data = np.array([35, 42, 36, 33, 31, 40, 33, 35, 47, 33, 30])
# variance = np.var(data)
# # Calculating standard deviation
# std_deviation = np.std(data)
# percentile_50 = np.percentile(data, 75)
# print(percentile_50)
# print(variance)
# print(std_deviation)

from sklearn.metrics import r2_score
X = [35, 42, 36, 33, 31, 40, 33, 35, 41, 33, 30,33.9,38.33]
Y = [34.9, 42, 35.9, 33, 31, 41, 33, 34.9, 41.5, 32, 29.5,33.89,38.351]
#calcola il coefficiente di determinazione tra i dati X e quelli stimati
# Assuming y_true contains the observed values and y_pred contains the predicted values
r2 = r2_score(X, Y)
print("R-squared:", r2)
print(f'La moda di X:{statistics.mode(X)}')
print(f'La moda di Y:{statistics.mode(Y)}')
print(f'Riordino la distrubuzione {sort(X)}')
print(f'La mediana di X: {statistics.median(X)}')
print(f'La covarianza tra X e Y :{statistics.covariance(X,Y)}')

Y = np.array([35,42,36,33,31,40,33,35,41,33,30,33.9,38.33])
X = np.array([34.9,42,35.9,33,31,41,32,34.9,41.5,32,29.5,33.89,38.35])
plt.xlabel("ASCISSA")
plt.ylabel("ORDINATA")
plt.grid()
plt.scatter(X,Y)
plt.show()