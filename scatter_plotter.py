import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
ypoints = np.array([99,95,98,96,92,99,97,96,99,96,97,98,97])
plt.xlabel("ASCISSA")
plt.ylabel("ORDINATA")
plt.grid()
plt.scatter(x, ypoints)
plt.bar(x,ypoints)
plt.show()
plt.show()
plt.plot(ypoints, marker = 'o')
plt.grid()
plt.show()