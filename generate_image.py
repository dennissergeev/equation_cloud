import matplotlib as mpl

mpl.use("pgf")
pgf_with_custom_preamble = {
    "font.family": "serif", # use serif/main font for text elements
    "text.usetex": True,    # use inline math for ticks
    "pgf.rcfonts": False,   # don't setup fonts from rc parameters
    "pgf.preamble": [
"\\usepackage{mathspec}",
r"\setmainfont{whatever it takes}",
r"\setmathsfont(Digits,Latin,Greek)[Numbers={Lining,Proportional}]{whatever it takes}"
         #"\\usepackage{eulervm}",
         # "\\usepackage{units}",         # load additional packages
         # "\\usepackage{metalogo}",
         # "\\usepackage{unicode-math}",  # unicode math setup
         # r"\setmathfont{xits-math.otf}",
         # r"\setmainfont{DejaVu Serif}", # serif font via preamble
         ]
}
mpl.rcParams.update(pgf_with_custom_preamble)

import matplotlib.pyplot as plt
import numpy as np


eqs = []
eqs.append((r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + "
            r"\frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

fig, ax = plt.subplots(figsize=(10,10), facecolor='r')

for i in range(50):
    idx = np.random.randint(0, len(eqs))
    eq = eqs[idx]
    size = np.random.uniform(12, 32)
    x, y = np.random.uniform(0, 1, 2)
    alpha = np.random.uniform(0.5, .95)
    ax.text(x, y, eq, ha='center', va='center', color="red", alpha=alpha,
            transform=ax.transAxes, clip_on=True)

ax.axis('off')
#ax.set_axis_bgcolor('black')
plt.savefig('figure.pdf')
