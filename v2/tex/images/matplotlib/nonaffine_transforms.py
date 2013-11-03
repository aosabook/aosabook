#!/usr/bin/env python
from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams['font.size'] = 8
rcParams['font.family'] = "Times New Roman"

fig = plt.figure(figsize=(6, 2))

x = np.linspace(0, 4*np.pi, 100)
y = np.linspace(0, 1, 100)

ax = fig.add_subplot(131)
ax.plot(x, y)
ax.set_xscale('log')

ax = fig.add_subplot(132, polar=True)
ax.plot(x, y)
ax.set_rticks([0, 0.5, 1.0])

ax = fig.add_subplot(133, projection="lambert")
ax.grid(True)
ax.set_xticks([-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2])
ax.plot(x, y)

fig.savefig("nonaffine_transforms.pdf")
