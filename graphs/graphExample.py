import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# multiple points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, marker='o')
# plt.plot(xpoints, ypoints, 'o') # plot only markers

# The x-points in the example above is [0, 1, 2, 3, 4, 5] if left out

plt.show()
