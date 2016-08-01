# -*- coding: utf-8 -*-
from preamble import load
load()
import matplotlib.pyplot as plt  # NOQA
import numpy as np  # NOQA


eqs = []
with open("equations.tex") as f:
    for line in f.read().splitlines():
        eq = r"${}$".format(line)
        eqs.append(eq)

facecolor = '#000000'
fontcolor = '#1234AB'

fig, ax = plt.subplots(figsize=(10, 10))
txt_dict = dict(ha='center', va='center', color=fontcolor,
                transform=ax.transAxes, clip_on=True)

for i in range(5):
    idx = np.random.randint(0, len(eqs))
    eq = eqs[idx]
    size = np.random.uniform(12, 32)
    x, y = np.random.uniform(0, 1, 2)
    alpha = np.random.uniform(0.5, .95)
    ax.text(x, y, eq, alpha=alpha, **txt_dict)

ax.axis('off')
fig.savefig('figure.pdf', facecolor=facecolor)
