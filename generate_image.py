# -*- coding: utf-8 -*-
from preamble import load
load()
import matplotlib.pyplot as plt  # NOQA
import matplotlib.patheffects as PathEffects  # NOQA
import numpy as np  # NOQA


eqs = []
with open("equations.tex") as f:
    for line in f.read().splitlines():
        eq = r"${}$".format(line)
        eqs.append(eq)

facecolor = '#fff9ff'
fontcolor = '#333333'
# strokecolor = '#FFFFFF'

txt_dict = dict(ha='center', va='center', color=fontcolor,
                clip_on=True)
# pe_dict = dict(linewidth=1, foreground=strokecolor)

fig, ax = plt.subplots(figsize=(10, 10))

for eq in eqs:
    # idx = np.random.randint(0, len(eqs))
    # eq = eqs[idx]
    size = np.random.uniform(10, 30)
    x, y = np.random.uniform(0, 1, 2)
    alpha = np.random.uniform(0, 1)
    t = ax.text(x, y, eq, alpha=alpha, size=size,
                transform=ax.transAxes, **txt_dict)
    # t.set_path_effects([PathEffects.withStroke(**pe_dict)])


ax.axis('off')
fig.savefig('figure.pdf', facecolor=facecolor)
