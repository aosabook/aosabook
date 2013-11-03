# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

x = np.linspace(0, np.pi*2, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.title('A simple plot')
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
prop = font_manager.FontProperties(size=48)
plt.figtext(0.91, 0.9, ur'①', fontproperties=prop)
plt.figtext(0.81, 0.8, ur'②', fontproperties=prop)
plt.figtext(0.81, 0.52, ur'③', fontproperties=prop)
plt.figtext(0.62, 0.91, ur'④', fontproperties=prop)
plt.figtext(0.01, 0.3, ur'⑤', fontproperties=prop)
plt.figtext(0.58, 0.01, ur'⑥', fontproperties=prop)
plt.savefig('artists_figure.pdf')
