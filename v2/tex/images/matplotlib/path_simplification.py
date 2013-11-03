from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams['font.size'] = 8
rcParams['font.family'] = "Times New Roman"

points = 1024

np.random.seed(0)

x = np.linspace(0, 6, points)
y = (np.random.rand(points) - 0.5) * 2.0 * np.abs(np.sin(x))

fig = plt.figure(figsize=(6, 2))
ax = plt.subplot2grid((1,3), (0, 0), colspan=2)
ax.plot(x, y, '-')
ax.axvspan(4.9, 4.95, facecolor='k', alpha=0.2)

ax = plt.subplot2grid((1,3), (0, 2))
ax.plot(x[840], y[840], 'o', color='w', markersize=15)
ax.plot(x, y, '-o')
ax.set_xlim(4.900, 4.95)
ax.set_yticks([])

fig.savefig("path_simplification.pdf", bbox_inches="tight")
