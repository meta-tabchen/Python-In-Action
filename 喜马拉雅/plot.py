# import matplotlib.pyplot as plt
# y=[295, 290, 295, 298, 311, 284, 287, 307, 204, 29, 0, 0, 46, 203, 245, 228, 274, 264, 271, 268, 235, 234, 236, 239, 221]
# x=[3*x+3 for x in range(len(y))]
# plt.plot(x, y, 'ro')
# # plt.axis([0, 6, 0, 20])
# plt.show()
# x=[3*x*x+3 for x in range(len(y))]
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 1])
plt.ion()

for i in range(100):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.1)