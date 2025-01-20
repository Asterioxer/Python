import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 400)
y1 = x
y2 = np.sin(x)

plt.plot(x, y1, label='y = x')
plt.plot(x, y2, label='y = sin(x)')
plt.legend()
plt.show()