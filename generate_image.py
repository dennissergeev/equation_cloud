# -*- coding: utf-8 -*-
from preamble import load
load()
import matplotlib.pyplot as plt
import numpy as np


eqs = []
eqs.append((r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + "
            r"\frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

facecolor = 'k' # '#000000'
fontcolor = 'w' # '#1234AB'

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
