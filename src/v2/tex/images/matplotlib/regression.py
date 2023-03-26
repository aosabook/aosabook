from matplotlib import pyplot as plt

fig = plt.figure(figsize=(6,2))

for i, filename in enumerate([
    'expected-legend_auto2.png',
    'legend_auto2.png',
    'failed-diff-legend_auto2.png']):
    ax = fig.add_subplot(1, 3, i+1)
    im = plt.imread(filename)
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])

fig.savefig('regression.pdf', dpi=600, bbox_inches='tight')
