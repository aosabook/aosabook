from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['axes.linewidth'] = 1

plt.plot([1,2,3])
plt.yticks([])
plt.savefig("pixels_snapped.png", dpi=72)

plt.clf()

rcParams['path.snap'] = False
plt.plot([1,2,3])
plt.yticks([])
plt.savefig("pixels_unsnapped.png", dpi=72)

plt.clf()

rcParams['path.snap'] = True
rcParams['axes.linewidth'] = 0

fig = plt.figure(figsize=(4, 2))

for i, filename in enumerate(['pixels_unsnapped.png', 'pixels_snapped.png']):
    ax = fig.add_subplot(1, 2, i+1)
    im = plt.imread(filename)
    ax.imshow(im, interpolation='nearest')
    ax.set_xlim(70, 76)
    ax.set_ylim(46, 41)
    ax.set_xticks([])
    ax.set_yticks([])

fig.savefig("pixel_snapping.pdf", bbox_inches="tight")
